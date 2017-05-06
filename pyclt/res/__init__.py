#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pyclt.res.languages import *
import json
import os
def getText(language_type):
    '''获取语言字符'''
    if language_type =="zh_cn":
        return zh_cn()

