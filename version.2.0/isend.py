# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from threading import _sleep,Thread

#该模块用于检测歌曲是否播放完毕然后下一曲

class IsEnd(Thread):

    def __init__(s,music):
        Thread.__init__(s)
        s.setDaemon(True)
        s.__running = True
        s.__flag = True#暂停控制
        s.__music = music

    def stop(s):
        s.__running = False

    def pause(s):
        s.__flag = True#暂停
        print 'IsEnd Pause'

    def goon(s):
        s.__flag = False#继续
        print 'IsEnd Goon'

    def run(s):
        while s.__running:
            if not s.__running:
                break
            if s.__flag:#暂停
                continue
            try:
                #已播放时间
                _sleep(3)#每隔5秒
                if not s.__music.droid.mediaIsPlaying('zmusic').result:
                    #播放完毕
                    s.__music.autoNext()#这首歌曲播放完毕则下一曲
                #print 'Is Playing'
            except Exception,e:
                pass
