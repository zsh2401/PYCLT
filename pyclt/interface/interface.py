#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pyclt.api
import pyclt.res as res
class Interface():
    def __init__(self,__type):
        '''初始化API'''
        self.text = res.getText('zh_cn') 
        self.setApi(__type)
        
    def setApi(self,__type):
        '''初始化API'''
        self.text = res.getText('zh_cn') 
        if __type == 'netease':
            import pyclt.api.netease
            print(self.text['loading_netease'])
            self.api = pyclt.api.netease.Api()
            print(self.text['loaded_netease'])
            
            
        elif __type == 'netease_spider':
            print(self.text['loading_netease_spider'])
            import pyclt.api.neteasespider
            self.api = pyclt.api.neteasespider.Spider()
            print(self.text['loaded_netease_spider'])
            
        elif __type == 'baidu':
            import pyclt.api.baidu
            print(self.text['loading_baidu'])
            self.api = pyclt.api.baidu.Api()
            print(self.text['loaded_baidu'])
            
            
        elif __type == 'jinshan':
            import pyclt.api.jinshan
            print(self.text['loading_jinshan'])
            self.api = pyclt.api.jinshan.Api()
            print(self.text['loaded_jinshan'])
            
        