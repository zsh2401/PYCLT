#!/usr/bin/python3
# -*- coding:utf-8 -*-
from pyclt.interface.interface import Interface
import pyclt.res
import pyclt.api
import pyclt.api.jinshan
import webbrowser
try:
    from tkinter import *
    from tkinter.messagebox import *
except ImportError:
    print('找不到tkiner库!!!\n如果您是windows请重装python3\nlinux请使用包管理器安装python3-tk(注意:不是pip,是yum或apt-get)')
    sys.exit()
class GuiProgram(Interface):
    def __init__(self,api_type):
        super().__init__(api_type)
        self.__type__ = 'gui'
        self.__api_type = api_type
        self.__bg_color = '#70f3ff'
        self.__input_text_color = '#e0f0e9'
        self.__out_text_color = '#e0f0e9'
        self.__tans_button_color = 'white'
        self.__clear_button_color = 'white'
        self.__github_url = 'http://github.com/zsh2401/PYCLT'
        self.__donate_url = 'http://blog.csdn.net/zsh2401/article/details/71056205'
    def run(self):
        '''开始运行'''
        try:
            self.master = Tk()
            self.master.geometry('600x370')
            self.master.resizable(False, False)
            self.__packAny()
            self.master.mainloop()
        except ValueError:
            print(self.text['tk_error'])
    def __showAbout(self):
        '''显示开发者相关信息'''
        showinfo(title = self.text['messagebox_title'], message=self.text['gui_about'])
        
    def __showAboutVersion(self):
        '''显示版本相关信息'''
        showinfo(title=self.text['messagebox_title'],message=self.text['gui_about_version'])    
    
    def __showAboutOpenSource(self):
        '''显示开源相关信息'''
        webbrowser.open(self.__github_url, new=2, autoraise=True)
        showinfo(title=self.text['messagebox_title'],message=self.text['open_source'])
        
        
    def __openDonateWeb(self):
        '''调用系统默认浏览器打开捐赠网页'''
        webbrowser.open(self.__donate_url, new=2, autoraise=True)
        
    def __packAny(self):
        '''放置各种窗口组件'''
        self.__api_type_var = StringVar()
        self.__api_type_var.set(self.__api_type)#设置一个tkstringvar用于radiobutton进行选择
        
        self.frame = Frame(self.master,bg = self.__bg_color,height = 400,width = 600)
        self.frame.place(y = 0)
        
        self.master.title(self.text['app_name'])#窗口标题
        
        self.menubar = Menu(self.master,bg='yellow')
       
        self.menubar.add_command(label=self.text['about'],command=self.__showAbout)
        self.menubar.add_command(label=self.text['about_version'],command=self.__showAboutVersion)
        self.menubar.add_command(label=self.text['about_open_source'],command=self.__showAboutOpenSource)
        self.menubar.add_command(label=self.text['donate'],command=self.__openDonateWeb)
        self.master.config(menu=self.menubar) 

        self.entry_text = Text(self.master,bg=self.__input_text_color,width = 82,height=7)
        self.entry_text.place(x=15,y=25)
        
        self.out_text = Text(self.master,bg=self.__out_text_color,height=12,width = 82)
        self.out_text.place(x = 10,y=200)
        ###Radiobutton
        self.netease_radiobutton = Radiobutton(self.master,
                                    variable=self.__api_type_var,
                                    text = '网易有道翻译API',
                                    value='netease',
                                    bg=self.__bg_color,
                                    command=self.__resetApi)
        self.netease_radiobutton.place(x=20,y=120)
        
        self.baidu_radiobutton = Radiobutton(self.master,
                                    variable=self.__api_type_var,
                                    text = '百度翻译API',
                                    value='baidu',
                                    bg=self.__bg_color,
                                    command=self.__resetApi)
        self.baidu_radiobutton.place(x=160,y=120)
        
        self.jinshan_radiobutton = Radiobutton(self.master,
                                    variable=self.__api_type_var,
                                    text = '金山词霸翻译API',
                                    value='jinshan',
                                    bg=self.__bg_color,
                                    command=self.__resetApi)
        self.jinshan_radiobutton.place(x=294,y=120)
        
        self.neteasesp_radiobutton = Radiobutton(self.master,
                                    variable=self.__api_type_var,
                                    text = '网易有道翻译爬虫',
                                    value='netease_spider',
                                    bg=self.__bg_color,
                                    command=self.__resetApi)
        self.neteasesp_radiobutton.place(x=430,y=120)
        ###Radiobutton
        
        self.tans_button = Button(self.master,text=self.text['tans'],
                                width=50,height=2,
                                bg=self.__tans_button_color,
                                command = self.__tans
                            )
        self.tans_button.place(x=20,y=150)
        self.clear_button = Button(self.master,text=self.text['clear'],
                                width=20,height=2,
                                bg=self.__clear_button_color,
                                command = self.__clear_text
                                )
        self.clear_button.place(x=400,y=150)
        
    def __clear_text(self):
        '''清空输入输出框 '''
        self.entry_text.delete(0.0, END)
        self.out_text.delete(0.0, END)
        
    def __resetApi(self):
        self.out_text.delete(0.0, END)
        self.setApi(self.__api_type_var.get())
        
    def __tans(self):
        if self.entry_text.get(0.0, END) != '':
            showinfo(title = '提示',message=self.text['loading'])
            result = self.api.getGuiResult(self.entry_text.get(0.0, END))
            self.out_text.delete(0.0, END)
            self.out_text.insert('end',result)
        else:
            showinfo(title = '提示',message=self.text['please_input'])

        
if __name__ == '__main__':
    _type = 'netease'
    print(_type)
    gui = GuiProgram(_type)
    gui.run()
