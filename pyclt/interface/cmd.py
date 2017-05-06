#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pyclt.interface.interface import Interface
class CmdProgram(Interface):
    def __init__(self,word,__type):
        '''进行继承'''
        super().__init__(__type)
        self.word = word
        self.__type__ = 'gui'
        
    def run(self):
        '''进行翻译'''
        result = self.api.getCmdResult(self.word)
        print(result)
        
