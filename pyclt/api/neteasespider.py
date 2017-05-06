#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import json
import pyclt.res
import pyclt.api
class Spider(pyclt.api.Api):
    '''爬虫版翻译程序'''
    def __init__(self):
        super().__init__()
        self.__url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        
    def getCmdResult(self,word):
        dict_data = self.__getDictData(word)
        string = (self.text['simple_header'] + '\n' + self.text['translation'] + '>>\t' + self.__DictData2Result(dict_data))
        return string
        
    def getGuiResult(self,word):
        return self.getCmdResult(word)
        
    def __getDictData(self,word):
        data = {}
        data['type'] = 'AUTO'
        data['i'] = str(word)
        data['doctype'] = 'json'
        data['xmlVersion'] = '1.8'
        data['keyfrom'] = 'fanyi.web'
        data['ue'] = 'UTF-8'
        data['action'] = 'FT_BY_ENTER'
        data = urllib.parse.urlencode(data).encode('utf-8')
        head = {}
        head['User-Agent'] = 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
        return json.loads(urllib.request.urlopen(self.__url,data).read().decode('utf-8'))
        
    def __DictData2Result(self,dict_data):
        for key,value in dict_data.items():
            if key == 'translateResult':
                for x_key,x_value in value[0][0].items():
                    if x_key =='tgt':
                        return x_value