#!/usr/bin/python3
# -*- coding:utf-8 -*-

from setuptools import setup
#
#哈哈!!
setup(
    name='pyclt',
    version='0.7.5',
    author='zsh2401',
    author_email='zsh2401@163.com',
    url='https://github.com/zsh2401/PYCLT',
    description='一个快捷的命令行翻译软件!按照GPL-3.0协议开源!',
    packages=['pyclt','pyclt.res','pyclt.interface','pyclt.api'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'cltb=pyclt:run4baiduApi',
            'cltj=pyclt:run4jinshanApi',
            'cltn=pyclt:run4neteaseApi',
            'clts=pyclt:run4neteaseSpider',
            'pyclt=pyclt:run4pyclt',
        ]
    },
    classifiers = [
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
      ]
)
