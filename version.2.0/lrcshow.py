# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from threading import Thread
from lrcparse import getLrc

class LrcShow(Thread):

    def __init__(s,music):
        Thread.__init__(s)
        s.setDaemon(True)
        s.__running = True
        s.__flag = True#暂停控制
        s.__music = music
        s.__lrcTime = []
        s.__lrcData = {}
        s.__position = 0
        s.__index = 0

    def init(s,path):
        s.__position = 0
        s.__index = 0
        s.__lrcTime = []
        s.__lrcData = {}
        try:
            s.__lrcTime,s.__lrcData = getLrc(path[:-4]+'.lrc')
        except Exception,e:
            s._clearLrc()
        s.__flag = False#继续

    def setPos(s,pos):
        s.__position = pos

    def _clearLrc(s):
        s.__music.setProperty('music_main_lrc_text1','text','')
        s.__music.setProperty('music_main_lrc_text2','text','')
        s.__music.setProperty('music_main_lrc_text3','text','')

    def _setViewLrc(s,one,two,three):
        s.__music.setProperty('music_main_lrc_text1','text',one)
        s.__music.setProperty('music_main_lrc_text2','text',two)
        s.__music.setProperty('music_main_lrc_text3','text',three)

    def stop(s):
        s.__running = False

    def pause(s):
        s.__flag = True#暂停

    def goon(s):
        s.__flag = False#继续

    def run(s):
        while s.__running:
            if not s.__running:
                break
            if s.__flag:#暂停
                continue
            if s.__lrcTime:
                try:
                    value = s.__lrcTime[s.__index]
                    one=two=three = ''
                    Time = value + 1 - s.__position
                    #if Time > 0 and Time < 1:
                    if s.__position <= value + 1:#当前播放了的时间<歌词显示的时间#2<3
                        try:
                            one = s.__lrcData.get(s.__lrcTime[s.__index]);print one
                        except:
                            pass
                        try:
                            two = s.__lrcData.get(s.__lrcTime[s.__index+1])#尝试获取下一行歌词
                        except:
                            pass
                        try:
                            three = s.__lrcData.get(s.__lrcTime[s.__index+2])#尝试获取下一行歌词
                        except:
                            pass
                        s._setViewLrc(one,two,three)
                    else:
                        s.__index += 1
                except:
                    pass
