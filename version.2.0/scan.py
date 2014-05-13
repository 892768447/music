# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from os import walk,remove
from os.path import join,getsize,splitext,getctime
from time import time
from threading import Thread
from config import ScanPath,CurrentPath,MusicListPath,MusicSize,ExtList
#载入配置文件中的扫描路径
from waitbar import WaitBar
#载入进度条模块

class Scan(Thread):

    def __init__(s,music):
        Thread.__init__(s)
        s.setDaemon(True)
        s.__running = False
        s.__music = music
        s.__waitbar = WaitBar(music)

    def stop(s):
        s.__running = False
    
    def delete(s):
        try:
            remove(MusicListPath)
        except:
            pass

    def run(s):
        s.__running = True
        try:#检测歌曲列表创建时间是否在当天,是则不扫描
            if (time() - getctime(MusicListPath)) < 1*24*60*60:
                #说明歌曲列表创建时间在当天所以不扫描歌曲列表
                return
        except Exception,e:
            print e
        s.__waitbar.start()#启动进度条动画
        s.__music.setProperty('music_list_loading','visibility','visible')#显示进度条控件
        while s.__running:
            if not s.__running:
                s.__waitbar.stop()
                break
            '''
            mlv = s.__music.queryDetail('music_list','visibility')
            #查询歌曲列表界面是否显示
            if not mlv:
                s.__music.setProperty('music_list_loading','visibility','gone')#隐藏进度条控件
                s.__waitbar.pause()#暂停进度线程动画
            elif mlv == 'gone':#没有显示
                s.__music.setProperty('music_list_loading','visibility','gone')#隐藏进度条控件
                s.__waitbar.pause()#暂停进度线程动画
            else:
            '''
            #s.__waitbar.goon()#继续动画
            Dict = {0:('刷新歌曲列表','')}
            num = 1#从1开始0给刷新列表用
            for root,dirs,files in walk(ScanPath):
                for name in files:
                    if splitext(name)[1] in ExtList:#判断文件类型
                        path = join(root,name)
                        if getsize(path) > MusicSize:#文件大小大于1M
                            Dict[num] = (name,path)#{0:('name','path')}
                            num = num + 1
                        del path
            if Dict:
                open(MusicListPath,'wb').write(str(Dict))
            s.__waitbar.stop()#停止进度动画
            s.__music.setProperty('music_list_loading','visibility','gone')#隐藏进度条控件
            s.__music.music_dict = Dict
            s.__music.music_list = [Dict.get(key)[0] for key in Dict.keys()]
            #保持和music模块中的歌曲列表同步
            s.__music.setList('music_list_list',s.__music.music_list)
            #设置歌曲列表
            s.__running = False
            del Dict,num
            break
