# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from threading import Thread
#from discshow import DiscShow
#from lrcshow import LrcShow
#from progressbar import ProgressBar
#from endtime import EndTime

#界面卡事件响应不及时
#所以暂时去掉旋转和歌词和获取歌曲播放进度

#class Play(Thread):
class Play(object):

    def __init__(s,music):
        #Thread.__init__(s)
        #s.setDaemon(True)
        s.__first = True#第一次实例化?
        #s.__music_time = 9999999
        #歌曲播放进度条有关
        s.__music = music#主程序实例
        #s.__discshow = DiscShow(music)#圆碟转动线程
        #s.__lrcshow = LrcShow(music)#歌词显示线程
        #s.__progressbar = ProgressBar(music,s)#播放进度线程
        #s.__endtime = EndTime(music,s)#设置总时间线程

    '''
    def setMusicTime(s,time):
        s.__music_time = time

    def getMusicTime(s):
        return s.__music_time

    def setPosition(s,position):
        #从播放进度线程得到当前歌曲已经播放了多少秒
        #然后设置歌词显示线程中的position
        s.__lrcshow.setPos(position)
    '''
        
    def play(s,path):
        if s.__first:#第一次创建歌词线程,以后不再创建
            #s.__endtime.start()
            #s.__discshow.start()
            #s.__progressbar.start()
            #s.__lrcshow.start()
            s.__first = False
        s.__music.droid.mediaPlayClose('zmusic')#关闭当前播放的歌曲
        s.__music.droid.mediaPlay(path,'zmusic',True)#True立即播放歌曲False-调用mediaPlayStart('zmusic')播放
        #s.__discshow.goon()
        #接下来需要获取歌曲总时间
        #s.__endtime.goon()
        #播放进度显示
        #s.__progressbar.goon()
        #解析显示歌词文件
        #s.__lrcshow.init(path)#初始化

    def pause(s):
        s.__music.droid.mediaPlayPause('zmusic')#暂停播放
        #s.__endtime.pause()
        #s.__discshow.pause()
        #s.__progressbar.pause()
        #s.__lrcshow.pause()

    def goon(s):
        s.__music.droid.mediaPlayStart('zmusic')#继续播放
        #s.__endtime.goon()
        #s.__discshow.goon()
        #s.__progressbar.goon()
        #s.__lrcshow.goon()
    
    def stop(s):
        s.__music.droid.mediaPlayClose('zmusic')
        #s.__endtime.stop()
        #s.__discshow.stop()
        #s.__progressbar.stop()
        #s.__lrcshow.stop()
