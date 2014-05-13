# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from threading import Thread

class EndTime(Thread):

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
                #总时间
                result = s.__music.droid.mediaPlayInfo('zmusic').result
                if type(result) != type({}):
                    continue
                Time = result.get('duration')#eg:189262
                if not Time:
                    continue
                print 'endtime: Time: ',Time
                s.__play.setMusicTime(Time)#设置歌曲总时间
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
                s.__music.setProperty('music_main_play_time','text','00:00')
                s.__music.setProperty('music_main_end_time','text',minute + ':' + sec)
                del Time,minute,sec,result
                s.pause()
            except Exception,e:
                pass
