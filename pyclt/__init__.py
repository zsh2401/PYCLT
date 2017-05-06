#!/usr/bin/python3
# -*- coding:utf-8 -*-
__about__ ='''
About This Software
    Name : Python CommandLine Translators Python命令行翻译官 
    Version : 0.7.0
About Developer
    @zsh2401
    E-mail:     zsh2401@163.com
    Donate:     请输入cltn -donate进行捐赠
    GitHub:     github.com/zsh2401
'''
__help__ = '''
-----------PYCLT Help Message----------
Python CommandLine Translators
Python命令行翻译官

cltn [command or text]  使用网易API
cltb [command or text]  使用百度API
cltj [command or text]  使用金山API
clts [command or text]  使用网易爬虫

    -help       显示这个菜单
    -donate     打开捐赠网页
    -about      显示相关信息
    任何文字    翻译这段文字并且显示在命令行
    无参数      启动GUI版本的PYCLT
如果一个API无法使用或出现bug,可以试试别的!
'''

import sys
import os
import time
import platform
import webbrowser
import pyclt.res
from pyclt.interface.gui import GuiProgram
from pyclt.interface.cmd import CmdProgram
class Main():
    def __init__(self,sys_argv,__api_type = 'netease'):
        self.argv = sys_argv
        self.text = pyclt.res.getText("zh_cn")
        self.__api_type = __api_type
        self.__donate_url = 'http://blog.csdn.net/zsh2401/article/details/71056205'
        
    def run(self):
        '''开始运行程序'''
        if ("-help" in self.argv) or ("--help" in self.argv):
            print(__help__)
            sys.exit()
        elif ("-about" in self.argv) or ("--about" in self.argv):
            print(__about__)
            sys.exit()
        elif ("-d" in self.argv) or ("-donate" in self.argv):
            webbrowser.open(self.__donate_url, new=2, autoraise=True)
            sys.exit()
        elif len(self.argv) == 1 and self.__api_type != 'nothing':
            try:
                import tkinter as tk
                self.pyclt = GuiProgram(self.__api_type)
            except ImportError:
                print('找不到tkiner库!!!\n如果您是windows请重装python3\nlinux请使用包管理器安装python3-tk(注意:不是pip,是yum或apt-get)')
                sys.exit(1)
        elif self.__api_type != 'nothing':
            self.pyclt = CmdProgram(sys.argv[1],self.__api_type)
            
        elif (self.__api_type == 'nothing'):
            print(__help__)
            sys.exit()
            
        self.pyclt.run()
        
        if self.pyclt.__type__ == 'cmd' : 
            print('<---------------->')
            if platform.system() =='Windows':
                print(self.text['windowsPS'])
                print('<---------------->')
                
            if len(sys.argv) >= 3:
                print(self.text['more_arg'])
            
def run4pyclt():
    main = Main(sys.argv,'nothing')
    main.run()

def run4neteaseApi():
    main = Main(sys.argv,'netease')
    main.run()
def run4jinshanApi():
    main = Main(sys.argv,'jinshan')
    main.run()
def run4baiduApi():
    main = Main(sys.argv,'baidu')
    main.run()
def run4neteaseSpider():
    main = Main(sys.argv,'netease_spider')
    main.run()
