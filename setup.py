#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='requests-data',
    version='1.0',
    description="'data' URL scheme support for the popular Requests HTTP library.",
    long_description="'data' URL scheme support for the popular Requests HTTP library.",
    author='Jayson Vantuyl',
    author_email='jayson@aggressive.ly',
    url='https://github.com/jvantuyl/requests-data',
    packages=['requests_data'],
    package_data={'': ['LICENSE',]},
    include_package_data=True,
    install_requires=['requests>=1.1.0'],
    license=open('LICENSE').read(),
    zip_safe=True,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ),
)
