#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function

from setuptools import setup, find_packages

__version__ = 0.1

METADATA = dict(
    name='shadow',
    version=__version__,
    author='chen chiyuan',
    author_email='chenchiyuan03@.com',
    description='Utilities libs of my own.',
    long_description=open('README.md').read(),
    url='http://github.com/chenchiyuan/shadow',
    keywords='util python',
    install_requires=open('requirements').read().split('\n'),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    packages=find_packages(),
)

if __name__ == '__main__':
    setup(**METADATA)

