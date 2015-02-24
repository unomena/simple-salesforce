"""Simple-Salesforce Package Setup"""

from setuptools import setup
import textwrap
import sys

extra_install_requires = []
extra_tests_require = []
if sys.version_info < (2, 7):
    extra_install_requires.append('ordereddict>=1.1')
    extra_tests_require.append('unittest2>=0.5.1')

if sys.version_info < (3, 0):
    extra_tests_require.append('mock==1.0.1')

setup(
    name='simple-salesforce',
    version='0.66.3',
    author='Nick Catalano',
    packages=['simple_salesforce',],
    url='https://github.com/neworganizing/simple-salesforce',
    license='Apache 2.0',
    description=("Simple Salesforce is a basic Salesforce.com REST API client. "
        "The goal is to provide a very low-level interface to the API, "
        "returning an ordered dictionary of the API JSON response."),
    long_description=textwrap.dedent(open('README.rst', 'r').read()),
    install_requires=[
        'requests'
    ] + extra_install_requires,
    tests_require=[
        'nose>=1.3.0',
        'pytz>=2014.1.1'
    ] + extra_tests_require,
    test_suite = 'nose.collector',
    keywords = "python salesforce salesforce.com",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
