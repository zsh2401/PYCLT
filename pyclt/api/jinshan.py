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
        self.__type_ = "baidu"
        self.__key = 'B02E6E513E82D963255E970AE29C8D1B'
        self.__url_part1 = 'http://dict-co.iciba.com/api/dictionary.php?w='
        self.__url_part2 = '&type=json&key=' + self.__key
        self.header = ('>>>\t' + self.text['app_name'] + 
                    '\n>>>\t' + 'JinShan Api   ' + self.text['dever'])
        
    def __errorCodeExp(self,error_code):
        '''API返回错误代码处理'''
        return None
        
    def __getDictData(self,word):
        '''从api读取网页代码并转为字典'''
        word = urllib.parse.quote(word)
        web_code = urllib.request.urlopen(self.__url_part1 + word + self.__url_part2).read().decode('utf-8')
        dict_data = json.loads(web_code)
        return dict_data
        
    def getGuiResult(self,word):
        '''获取给gui使用的字符串'''
        return self.__getAllResult(word)
        
    def getCmdResult(self,word):
        '''获取给cmd使用的字符串'''
        return self.header + '\n' +  self.__getAllResult(word)
        
    def __getAllResult(self,word):
        dict_data = self.__getDictData(word)
        result = ''
        try:
            if 'is_CRI' in dict_data:#如果是英转中
                if 'word_name' in dict_data:
                    result = (self.text['query'] + '{0[word_name]}'.format(dict_data))
                
                #解析exchange
                if 'exchange' in dict_data:
                    if dict_data['exchange']['word_pl'] != '':
                        result += '\n' + self.text['xingtai']
                        result += '\n\t' + self.text['word_pl'] + dict_data['exchange']['word_pl'][0]
                    if dict_data['exchange']['word_past'] != '':
                        result += '\n\t' + self.text['word_past'] + dict_data['exchange']['word_past'][0]
                    if dict_data['exchange']['word_done'] != '':
                        result += '\n\t' + self.text['word_done'] + dict_data['exchange']['word_done'][0]
                    if dict_data['exchange']['word_ing'] != '':
                        result += '\n\t' + self.text['word_ing'] + dict_data['exchange']['word_ing'][0]
                    if dict_data['exchange']['word_third'] != '':
                        result += '\n\t' + self.text['word_third'] + dict_data['exchange']['word_third'][0]
                    if dict_data['exchange']['word_er'] != '':
                        result += '\n\t' + self.text['word_er'] + dict_data['exchange']['word_er'][0]
                    if dict_data['exchange']['word_est'] != '':
                        result += '\n\t' + self.text['word_est'] + dict_data['exchange']['word_est'][0]
                #解析发音
                if 'ph_en' in dict_data['symbols'][0]:
                    if 'ph_en' in dict_data['symbols'][0] and dict_data['symbols'][0]['ph_en'] != '':
                        result += '\n' + self.text['phonetic']
                        result += '\t' + self.text['uk-phonetic'] + dict_data['symbols'][0]['ph_en']
                if 'ph_am' in dict_data['symbols'][0]:
                    if dict_data['symbols'][0]['ph_am'] != '':
                        result += '\n\t' + self.text['us-phonetic'] + dict_data['symbols'][0]['ph_am']
                #解析其它词义
                if 'parts' in dict_data['symbols'][0]:
                    result += '\n' + self.text['explains']
                    for part in dict_data['symbols'][0]['parts']:
                        result += '\n\t' + part['part'] 
                        for part_part in part['means']:
                            result += '|' + part_part
            else:#如果是中转英
                #原词
                if 'word_name' in dict_data:
                    result = (self.text['query'] + ' : ' + '{0[word_name]}'.format(dict_data))
                #解析更多
                if 'symbols' in dict_data:
                    #解析发音
                    if 'word_symbol' in dict_data['symbols'][0]:
                        result += '\n' + self.text['phonetic'] + ' : ' + dict_data['symbols'][0]['word_symbol']
                    #解析中转英的更多释义
                    if 'parts' in dict_data['symbols'][0] and 'means' in dict_data['symbols'][0]['parts'][0]:
                        result += '\n' + self.text['more_ex']
                        for means in dict_data['symbols'][0]['parts'][0]['means']:
                            result += '\n\t' + means['word_mean']
            return result
        except:
            return '返回值错误'
'''
{'word_id': '2444434', 
'word_name': '我', 
'symbols': [
    {'symbol_id': '2445930', 
    'word_id': '2444434', 
    'word_symbol': 'wǒ', 
    'symbol_mp3': 'http://res.iciba.com/hanyu/zi/f18afb52f592712c250ad941b06da052.mp3',
    'parts': [{'part_name': '', 
            'means': [
            {'mean_id': '2953059', 'part_id': '2450485', 'word_mean': 'I', 'has_mean': '1', 'split': 1},
            {'mean_id': '2953060', 'part_id': '2450485', 'word_mean': 'me', 'has_mean': '1', 'split': 1}, 
            {'mean_id': '2953061', 'part_id': '2450485', 'word_mean': 'myself', 'has_mean': '1', 'split': 0}
                     ]
               }
             ], 
            'ph_am_mp3': '',
            'ph_en_mp3': '', 
            'ph_tts_mp3': '', 
            'ph_other': ''
    }
            ]
}

金山词霸json数据示例
{'word_name': 'word', 
'is_CRI': 1, 
'exchange': 
    {'word_pl': ['words'],        
    'word_past': ['worded'], 
    'word_done': ['worded'], 
    'word_ing': ['wording'], 
    'word_third': ['words'], 
    'word_er': '', 
    'word_est': ''}, 
'symbols': [{'ph_en': 'wɜ:d', 
            'ph_am': 'wɜrd', 
            'ph_other': '', 
            'ph_en_mp3': 'http://res.iciba.com/resource/amp3/0/0/c4/7d/c47d187067c6cf953245f128b5fde62a.mp3', 
            'ph_am_mp3': 'http://res.iciba.com/resource/amp3/1/0/c4/7d/c47d187067c6cf953245f128b5fde62a.mp3', 
            'ph_tts_mp3': 'http://res-tts.iciba.com/c/4/7/c47d187067c6cf953245f128b5fde62a.mp3', 
            'parts': [{'part': 'n.', 'means': ['单词', '话语', '诺言', '消息']},
            {'part': 'vt.', 'means': ['措辞，用词', '用言语表达']}, 
            {'part': 'vi.', 'means': ['讲话']}]}],
 'items': ['']}
 

'''