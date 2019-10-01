# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

setup(
    name="flowai",
    version="0.0.2",
    description="Flow Python Client API",
    long_description_content_type='text/markdown',
    long_description=README,
    url="https://github.com/flow-artint/flowai",
    download_url="https://github.com/flow-artint/flow-python/archive/v0.0.2.tar.gz",
    packages=find_packages(),
    author="Rahul Bhalley",
    author_email="rahulbhalley@icloud.com",
    install_requires=[
        "requests",
        "validators",
    ],
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)