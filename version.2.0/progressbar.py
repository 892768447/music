# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from threading import Thread
from config import ProgressBarLength

class ProgressBar(Thread):

    def __init__(s,music,play):
        Thread.__init__(s)
        s.setDaemon(True)
        s.__running = True
        s.__flag = True#暂停控制
        s.__music = music
        s.__play = play

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
            try:
                #已播放时间
                result = s.__music.droid.mediaPlayInfo('zmusic').result
                if type(result) != type({}):
                    continue#未知原因导致获取数据错误
                Time = result.get('position')#eg:189
                if not Time:
                    continue
                #s.__play.setPosition(Time/1000)#当前歌曲已经播放了多少秒这个跟歌词显示关联
                #s.__music.setProperty('music_main_progressBar','text','_'*(Time/1000*ProgressBarLength/s.__play.getMusicTime()/1000))
                minute = Time/60000#eg:3分钟
                sec = (Time - minute*60000)/1000#eg:9秒
                if minute < 10:
                    minute = '0' + str(minute)
                else:
                    minute = str(minute)
                if sec < 10:
                    sec = '0' + str(sec)
                else:
                    sec = str(sec)
                #s.__music.setProperty('music_main_play_time','text',minute + ':' + sec)
                try:
                    if (Time - s.__play.getMusicTime()) >= 0:
                        s.__music.autoNext()#这首歌曲播放完毕则下一曲
                except:
                    pass
                del Time,minute,sec,result
            except Exception,e:
                pass
