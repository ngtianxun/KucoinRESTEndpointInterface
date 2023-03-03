#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name='kucoin-python-modified',
    version='v1.0.15',
    packages=['kucoinModified', 'kucoinModified/base_request', 'kucoinModified/margin', 'kucoinModified/market', 'kucoinModified/trade', 'kucoinModified/user',
              'kucoinModified/websocket', 'kucoinModified/ws_token', 'kucoinModified/isolatedMargin'],
    license="MIT",
    author='Arthur',
    author_email="luckily_star0826@hotmail.com",
    url='https://github.com/Kucoin/kucoin-python-sdk',
    description="kucoin-api-sdk-modified",
    install_requires=['requests', 'websockets'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
