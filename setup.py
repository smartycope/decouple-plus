# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(name='decouple_plus',
      version='3.8',
      description='Strict separation of settings from code.',
      long_description=open(README).read(),
      author="Copeland Carter", author_email="smartycope@gmail.com",
      license="MIT",
      py_modules=['decouple_plus'],
      zip_safe=False,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django',
          'Framework :: Flask',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],
      url='https://github.com/smartycope/decouple-plus',)
