# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from threading import _sleep,Thread
from config import DiscPath,DiscTotal

class DiscShow(Thread):

    def __init__(s,music):
        Thread.__init__(s)
        s.setDaemon(True)
        s.__running = True
        s.__flag = True
        s.__music = music

    def stop(s):
        s.__running = False

    def pause(s):
        s.__flag = True#暂停旋转

    def goon(s):
        s.__flag = False#继续旋转

    def run(s):
        while s.__running:
            if not s.__running:
                break
            if s.__flag:#暂停
                continue
            for i in range(DiscTotal[1]):
                s.__music.setProperty('music_main_disc_extern','src','file://' + DiscPath + DiscTotal[0]%i)
                _sleep(0.2)