# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from re import findall

def getLrc(path):
    time = []
    lrc = {}
    try:
        lines = open(path,'rb').readlines()
        for line in lines:
            for i in findall('\[(\d+):(\d+)\.(\d+)\](.*?)$',line):
                sec = int(i[0])*60+int(i[1])+int(i[2])/1000
                time.append(sec)
                lrc[sec] = i[3]
                #{'sec':'lrc'}秒,歌词
    except Exception,e:
        print e
    return time,lrc