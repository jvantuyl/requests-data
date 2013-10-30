from email.utils import formatdate
from traceback import format_exc
from urllib import unquote as url_unquote
from requests import Response
from requests.adapters import BaseAdapter
from requests.exceptions import RequestException, InvalidURL
from requests.hooks import dispatch_hook
from binascii import a2b_base64
from StringIO import StringIO


class UnsupportedFeature(RequestException):
    """Adapter doesn't support this feature."""


class DataAdapter(BaseAdapter):
    """adapter for Data URIs"""

    def send(self, request, stream=False, verify=None, cert=None, proxies=None,
            timeout=None):
        """issue request"""

        data = url_unquote(request.url[len('data:'):])

        if ',' not in data:
            raise InvalidURL('data URL missing comma')

        mime, content = data.split(',', 1)
        content = content.strip()

        base64 = False
        charset = None

        while ';' in mime:
            mime, encoding_spec = mime.rsplit(';', 1)
            encoding_spec = encoding_spec.strip()
            if encoding_spec == 'base64':
                base64 = True
            elif not encoding_spec.startswith('charset='):
                raise InvalidURL(
                    'unrecognized encoding parameter: %r' % encoding_spec
                )
            else:
                charset = encoding_spec[len('charset='):]

        try:
            if base64:
                content = a2b_base64(content)

            content_type = mime.strip()
            if charset:
                content_type += "; charset=" + charset

            response = Response()
            response.url = request.url
            response.headers['Date'] = formatdate(timeval=None, localtime=True)

            if request.method in ('GET', 'HEAD'):
                response.status_code = 200
                response.headers['Content-Length'] = len(content)
                response.headers['Last-Modified'] = formatdate()
                response.headers['Content-Type'] = content_type
                if charset:
                    response.encoding = charset
                response.raw = StringIO(str(content))
            else:
                response.status_code = 405
                response.headers['Status'] = '405 Method Not Allowed'
        except Exception:
            response.status_code = 500
            response.headers['Status'] = '500 Internal Server Error'
            response.raw = StringIO(format_exc())

        # context
        response.request = request
        response.connection = self

        # hooks
        response = dispatch_hook('response', request.hooks, response)

        # streaming
        if not stream:
            response.content

        return response

    def close(self):
        """close connection (currently doesn't do anything)"""
