# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

#该模块功能未完成

from threading import Thread
from config import MusicSearchUrl,MusicLrcUrl
from urllib import urlopen
from re import findall

always_safe = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
               'abcdefghijklmnopqrstuvwxyz'
               '0123456789' '_.-')
_safe_map = {}
for i, c in zip(xrange(256), str(bytearray(xrange(256)))):
    _safe_map[c] = c if (i < 128 and c in always_safe) else '%{:02X}'.format(i)
_safe_quoters = {}

def quote(s, safe='/'):
    if not s:
        if s is None:
            raise TypeError('None object cannot be quoted')
        return s
    cachekey = (safe, always_safe)
    try:
        (quoter, safe) = _safe_quoters[cachekey]
    except KeyError:
        safe_map = _safe_map.copy()
        safe_map.update([(c, c) for c in safe])
        quoter = safe_map.__getitem__
        safe = always_safe + safe
        _safe_quoters[cachekey] = (quoter, safe)
    if not s.rstrip(safe):
        return s
    return ''.join(map(quoter, s))

class Download(Thread):

    def __init__(s,name):
        Thread.__init__(s)
        s.setDaemon(True)
        s.__name = quote(name)#要搜索的歌曲名字,需要编码一下
        s.__running = False

    def stop(s):
        s.__running = False

    def run(s):
        s.__running = True
        while s.__running:
            if not s.__running:
                break
            try:
                json = urlopen(MusicSearchUrl%(s.__name,'')).read()
                jlist = findall('song_id:"(\d+)",song_name:"(.*?)".*?singer_name:"(.*?)".*?price:"(\d+)"',json)
                #得到[('1691101', '\xb6\xcf\xb5\xe3', '\xc8\xba\xd0\xc7', '250')]
                #返回的数据searchCallBack({result:"0",msg:"",totalnum:"23",curnum:"1",search:"断点",songlist:[{idx:"1",song_id:"1691101",song_name:"断点",album_name:"男声试音天碟",singer_name:"群星",location:"7",singer_id:"12920",album_id:"134197",price:"250"}]})
                #需要匹配出里面的歌曲id歌曲名和是否有歌词
            except Exception,e:
                print e
                s.__running = False
                break#搜索歌曲信息失败
