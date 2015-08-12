#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages
from djangocms_search import __version__
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
requirements = [str(ir.req) for ir in install_reqs]

template_patterns = [
    'templates/*.html',
    'templates/*/*.html',
    'templates/*/*/*.html',
]

package_data = dict(
    (package_name, template_patterns)
    for package_name in packages
)

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
]

setup(
    name='djangocms-search',
    version=__version__,
    description='Search Plugin for django CMS',
    author='Iurii Garmash',
    author_email='garmon1@gmail.com',
    url='https://github.com/garmoncheg/djangocms-search',
    packages=find_packages('djangocms_search'),
    package_data=package_data,
    install_requires=requirements,
    license='MTI',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False
)