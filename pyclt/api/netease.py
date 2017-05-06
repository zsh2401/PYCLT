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
        self.__type_ = "netease"
        self.__api_url =  'http://fanyi.youdao.com/openapi.do?keyfrom=CLtranslators&key=1196545424&type=data&doctype=json&version=1.1&q='
     
    def __errorCodeExp(self,error_code):
        '''API返回错误代码处理'''
        return self.text['code_' + str(error_code)]   
    
    def __getDictData(self,word):
        '''从api读取网页代码并转为字典'''
        word = urllib.parse.quote(word)#这里进行转码,这样就可以进行中转英或其他语言转中的翻译
        web_code = urllib.request.urlopen(self.__api_url + word).read().decode("utf-8")
        dict_data = json.loads(web_code)
        return dict_data
        
    def getGuiResult(self,word):
        dict_data =  self.__getDictData(word)
        try:
            if dict_data['errorCode'] == 0:#当api访问未发生错误,则制作一份人能看懂的东西
                result = (self.text['query']  + ' --> ' + dict_data['query'] + '\n' +
                            self.text['translation']  + ' --> ' + dict_data['translation'][0] + '\n'
                        )
                if 'basic' in dict_data:
                    if 'phonetic' in dict_data['basic']:
                        result += ' | ' + self.text['phonetic'] + ' - ' +  dict_data['basic']['phonetic']
                    if 'uk-phonetic' in dict_data['basic']:
                        result +=  ' | ' + self.text['uk-phonetic'] + ' - ' + dict_data['basic']['uk-phonetic']
                    if 'us-phonetic' in dict_data['basic']:
                        result +=  ' | ' + self.text['us-phonetic'] +  ' - ' + dict_data['basic']['us-phonetic']
                    if 'explains' in dict_data['basic']:
                        result += '\n' + self.text['explains'] + '\n'
                        for explain in dict_data['basic']['explains']:
                            result += '  ' + explain + '\n'
                if 'web' in dict_data:
                    result += '\n' + self.text['result_from_web'] + '\n'
                    for web_explain in dict_data['web']:
                        result += '  ' + web_explain['key'] +' : '
                        for explain in web_explain['value']:
                            result += explain +';'
                        result += '\n'
            else:#如果出现错误,则返回错误信息
                result = self.__errorCodeExp(dict_data['errorCode'])
            return result
        except ValueError:#捕捉到错误
            return self.text['SomeError']
    def test(self):
        print('OK')
    def getCmdResult(self,word):
        '''获取结果,并且将结果转换为人能看懂的文字'''
        #这里进行转码,这样就可以进行中转英或其他语言转中的翻译
        dict_data =  self.__getDictData(word)
        try:
            if dict_data['errorCode'] == 0:#当api访问未发生错误,则制作一份人能看懂的东西
                result = (
                                '\033[0m>>>  ' + self.text['app_name'] + ' --' +  self.text['version'] + '\n' +
                                '\033[0m>>>  ' + self.text['thanks'] + '  ' +  self.text['dever'] + '\n'
                                '\033[0m\033[1;36m' + self.text['query']  + ' --> ' + dict_data['query'] + '\033[0m' +'\n' +
                                '\033[0m\033[1;36m' + self.text['translation']  + ' --> ' + dict_data['translation'][0] + '\033[0m\n'
                                )
                result += '\033[4;34m'
                if 'basic' in dict_data:
                    if 'phonetic' in dict_data['basic']:
                        result += ' | ' + self.text['phonetic'] + ' - ' +  dict_data['basic']['phonetic']
                    if 'uk-phonetic' in dict_data['basic']:
                        result +=  ' | ' + self.text['uk-phonetic'] + ' - ' + dict_data['basic']['uk-phonetic']
                    if 'us-phonetic' in dict_data['basic']:
                        result +=  ' | ' + self.text['us-phonetic'] +  ' - ' + dict_data['basic']['us-phonetic']
                    result += '\033[0m'
                    if 'explains' in dict_data['basic']:
                        result += '\n' + self.text['explains'] + '\n\033[1;34m'
                        for explain in dict_data['basic']['explains']:
                            result += '  ' + explain + '\n'
                    result += '\033[0m'
                if 'web' in dict_data:
                    result += self.text['result_from_web'] + '\n\033[1;36m'
                    for web_explain in dict_data['web']:
                        result += '  ' + web_explain['key'] +' : '
                        for explain in web_explain['value']:
                            result += explain +';'
                        result += '\n'
                result += '\033[0m'
            else:#如果出现错误,则返回错误信息
                result = self.__errorCodeExp(dict_data['errorCode'])
            return result
        except:#捕捉到错误
            return self.text['SomeError']
    
