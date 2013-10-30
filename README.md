requests-data: Data Scheme for Requests
=======================================

'data' URL scheme support for the popular Requests HTTP Library.

Example:

    from requests import Session
    from requests_data.adapters import DataAdapter

    s = Session()
    s.mount('data://', DataAdapter())
    r = s.get('data:text/plain,This%20is%20some%text.')
    print(r.code)
    print(r.content)


Caveats
-------

Some versions of requests require a double-slash in any URL.  Since data URLs
don't require the slashes, you'll have to update to a version of requests
containing the following patch:

https://github.com/jvantuyl/requests/commit/90b37b30351cb8064aeafdfc442685590cdc9821


Authors
--------
Copyright (C) 2013, Jayson Vantuyl <jayson@aggressive.ly>
