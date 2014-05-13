# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from threading import _sleep,Thread
from config import LoadingPath,LoadingTotal

class WaitBar(Thread):

    def __init__(s,music):
        Thread.__init__(s)
        s.setDaemon(True)
        s.__running = False
        s.__flag = False
        s.__music = music

    def stop(s):
        s.__running = False

    def pause(s):
        s.__flag = True

    def goon(s):
        s.__flag = False

    def run(s):
        s.__flag = False
        s.__running = True
        while s.__running:
            if not s.__running:
                break
            if s.__flag:
                continue#如果暂停则跳出循环
            for i in range(LoadingTotal[1]):
                s.__music.setProperty('music_list_loading','src','file://' + LoadingPath + LoadingTotal[0]%i)
                _sleep(0.1)
        print '扫描进度条停止'