#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import json
import pyclt.res
import pyclt.api
class Api(pyclt.api.Api):
    def __init__(self):
        '''初始化'''
        super().__init__()
        self.__type__ = "baidu"
    def __errorCodeExp(self,error_code):
        '''API返回错误代码处理'''
        return None
    def __getDictData(self,word):
        '''从api读取网页代码并转为字典'''
        return None
    def getGuiResult(self,word):
        '''获取给gui使用的字符串'''
        return self.text['api_not_enable']
    def getCmdResult(self,word):
        '''获取给cmd使用的字符串'''
        return self.text['api_not_enable']
