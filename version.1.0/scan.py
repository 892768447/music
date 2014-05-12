# -*- coding: utf-8 -*-

__author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'

__copyright__ = 'Copyright (c) 2009, ざ凍結の→愛.'

__version__ = 'Version 1.0'

from os import walk,remove

class Scan:

  def __init__(s):
    s.MusicListPath = '/mnt/sdcard/ZceMusic/music.list'
    s.musicList = []
    s.musicName = []
    try:
      music = open(s.MusicListPath,'rb').read().split('\n')
      s.musicList = eval(music[0])
      s.musicName = eval(music[1])
    except:
      pass

  def getMusicList(s):
    return s.musicList

  def getMusicName(s):
    return s.musicName

  def scan(s,path):
    s.musicList = []
    s.musicName = []
    for i in walk(path):
      for j in i[2]:
        if j[-4:] == '.mp3' or j[-4:] == '.ogg':
          s.musicName.append(j)
          s.musicList.append(i[0]+j)
    remove(s.MusicListPath)
    open(s.MusicListPath,'wb').write(str(s.musicList)+'\n'+str(s.musicName))

if __name__ == '__main__':
  Scan().scan('/mnt/sdcard/我的音乐/')
