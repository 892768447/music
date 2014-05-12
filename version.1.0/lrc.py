# -*- coding: utf-8 -*-

__author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'

__copyright__ = 'Copyright (c) 2009, ざ凍結の→愛.'

__version__ = 'Version 1.0'

from re import findall

class Lrc:

    def __init__(s):
        s.lrcTime = []
        s.lrcText = []

    def __del__(s):
        del s.lrcTime
        del s.lrcText

    def addTime(s,time):
        s.lrcTime.append(int(time[1:3])*60 + int(time[4:6]) + int(time[7:9])/1000.0)

    def addText(s,text):
        s.lrcText.append(text)

    def getLrcTime(s):
        return s.lrcTime

    def getLrcText(s):
        return s.lrcText

    def lrc(s,path):
        s.lrcTime = []
        s.lrcText = []
        data = open(path,'rb').read()
        for i in findall('(\W\d+:\d+\.\d+\W)(.*?)\s+',data):
            s.addTime(i[0])
            s.addText(i[1])
