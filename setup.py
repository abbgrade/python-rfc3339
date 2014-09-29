try:
    from setuptools import setup
except:
    from distutils.core import setup

import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

import rfc3339

setup(name='rfc3339',
      version=rfc3339.__version__,
      py_modules=['rfc3339'],
      # metadata for upload to PyPI
      author=rfc3339.__author__,
      author_email=rfc3339.__author__,
      description='Format dates according to the RFC 3339.',
      long_description=rfc3339.__doc__,
      license=rfc3339.__license__,
      url='http://pypi.python.org/pypi/rfc3339/',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Topic :: Internet',
          'Intended Audience :: Developers',
          'Programming Language :: Python'],
      **extra
)
