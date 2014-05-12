# -*- coding: utf-8 -*-

__author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'

__copyright__ = 'Copyright (c) 2009, ざ凍結の→愛.'

__version__ = 'Version 1.0'

import android
import lrc
import math
import install
import thread as th
import scan
from time import sleep
from json import dumps
from musicxml import *
from listxml import *
from threading import Thread
from os.path import basename
from os import abort

install.install()
droid = android.Android()
lrc = lrc.Lrc()
scanMusic = scan.Scan()
droid.fullShow(Layout)
droid.fullSetTitle('ZceMusic音乐播放器')
droid.startSensingTimed(1, 200)

class Clear(Thread):

  def __init__(s):
    Thread.__init__(s)

  def run(s):
    while True:
      droid.eventClearBuffer()
      sleep(60)

class Show(Thread):

  def __init__(s,path):
    Thread.__init__(s)
    s.isLrcShow = False
    s.isPause = False
    try:
      lrc.lrc(path[:-4]+'.lrc')
      s.lrcTime = lrc.getLrcTime()
      s.lrcText = lrc.getLrcText()
    except:
      s.lrcTime = []
      s.lrcText = []

  def run(s):
    if len(s.lrcTime) == 0 or len(s.lrcText) == 0:
      droid.fullSetProperty('lrc', 'text', '没有歌词')
      th.exit()
    else:
      while True:
        sleep(s.lrcTime[0]-0)
        droid.eventPost('lrcShow', s.lrcText[0],True)
        i = 0
        while i < (len(s.lrcTime)-1):
          if s.isLrcShow:
            th.exit()
          if s.isPause:
            i = i - 1
          droid.eventPost('lrcShow', s.lrcText[i],True)
          sleep(s.lrcTime[i+1]-s.lrcTime[i])
          i = i + 1
        droid.eventPost('lrcShow',s.lrcText[-1],True)
        s.isLrcShow = True
        break

  def stop(s):
    s.isLrcShow = True
    #print 'stop'

  def pause(s):
    s.isPause = True
    #print 'pause'

  def play(s):
    s.isPause = False

class Play(Thread):

  def __init__(s,path):
    Thread.__init__(s)
    #print path
    s.show = Show(path)
    droid.mediaPlayClose('default')
    droid.mediaPlay(path, 'default', False)
    droid.fullSetProperty('title', 'text', basename(path))

  def run(s):
    #print 'play run'
    droid.fullSetProperty('lrc', 'text', '')
    droid.mediaPlayStart('default')

class Event(Thread):

  def __init__(s):
    Thread.__init__(s)
    s.position = 0
    s.stopBtn = False
    s.leftValue = 0
    s.rightValue = 0
    s.name = ''
    s.musicList = scanMusic.getMusicList()
    s.musicName = scanMusic.getMusicName()
    Clear().start()
    s.show = Show('')
    s.show.start()

  def scanMusic(s):
    if len(s.musicList) == 0 or len(s.musicName) == 0:
      while True:
        path = droid.dialogGetInput('歌曲搜索', '请输入搜索路径', '/mnt/sdcard/我的音乐/').result
        if path != None:
          if len(path) != 0:
            droid.makeToast('扫描歌曲中')
            scanMusic.scan(path.encode('utf-8'))
            s.musicList = scanMusic.getMusicList()
            s.musicName = scanMusic.getMusicName()
            droid.fullSetList('list', s.musicName)
            break
        else:
          s.musicList = scanMusic.getMusicList()
          s.musicName = scanMusic.getMusicName()
          break
    else:
      droid.fullSetList('list', s.musicName)

  def itemclick(s,event):
    if event['name'] == 'itemclick':
      droid.fullDismiss()
      droid.fullShow(Layout)
      droid.fullSetTitle('ZceMusic音乐播放器')
      s.position = int(event['data']['position'])
      s.name = s.musicList[s.position]
      Play(s.name).start()
      s.show.stop()
      s.show = Show(s.name)
      s.show.start()

  def sensors(s,event):
    if event['name'] == 'sensors':
      value = int(event['data']['roll']*60.0/math.pi*4)
#右为正，左为负
      if value >= 0:
        s.rightValue = value
      if value <= 0:
        s.leftValue = value
      if s.rightValue > 50 and s.leftValue < -50:
        s.rightValue = 0
        s.leftValue = 0
        if s.position < len(s.musicList) - 1:
          s.position = s.position + 1
          s.name = s.musicList[s.position]
          Play(s.name).start()
          s.show.stop()
          s.show = Show(s.name)
          s.show.start()
        else:
          s.position = len(s.musicList) - 1

  def listen(s,id):
    if id == 'left':
      droid.fullDismiss()
      droid.fullShow(ListLayout)
      droid.fullSetTitle('ZceMusic音乐播放器')
      s.scanMusic()
  
    if id == 'right':
      droid.fullDismiss()
      droid.fullShow(Layout)
      droid.fullSetTitle('ZceMusic音乐播放器')
      droid.fullSetProperty('title', 'text', basename(s.name))

    if id == 'refresh':
      s.musicList = []
      s.musicName = []
      s.scanMusic()

    if id == 'exit':
      droid.makeToast('谢谢下次使用')
      droid.forceStopPackage('com.googlecode.android_scripting')
      droid.forceStopPackage('com.googlecode.pythonforandroid')
      abort()

    if id == 'play':
      if not droid.mediaIsPlaying('default').result:
        if s.stopBtn:
          s.stopBtn = False
          s.name = s.musicList[s.position]
          Play(s.name).start()
          s.show.stop()
          s.show = Show(s.name)
          s.show.start()
        else:
          droid.mediaPlayStart('default')
          s.show.play()

    if id == 'pause':
      droid.mediaPlayPause('default')
      s.show.pause()

    if id == 'stop':
      droid.mediaPlayClose('default')
      s.stopBtn = True
      s.show.stop()

    if id == 'on':
      s.on()

    if id == 'next':
      s.next()

    if id == 'rewind':
      result = droid.mediaPlayInfo('default').result
      if result['loaded']:
        position = result['position'] - 10000
        if position > 0:
          droid.mediaPlaySeek(position,'default')
        else:
          s.on()

    if id == 'forward':
      result = droid.mediaPlayInfo('default').result
      if result['loaded']:
        position = result['position'] + 10000
        if position < result['duration']:
          droid.mediaPlaySeek(position,'default')
        else:
          s.next()

  def on(s):
    if s.position > 0:
      s.position = s.position - 1
      s.name = s.musicList[s.position]
      Play(s.name).start()
      s.show.stop()
      s.show = Show(s.name)
      s.show.start()
    else:
      s.position = 0

  def next(s):
    if s.position < len(s.musicList) - 1:
      s.position = s.position + 1
      s.name = s.musicList[s.position]
      Play(s.name).start()
      s.show.stop()
      s.show = Show(s.name)
      s.show.start()
    else:
      s.position = len(s.musicList) - 1

  def run(s):
    #print 'event run'
    while True:
      event = droid.eventWait().result
      if event == True or event == False or event == 'OK' or event == None:
        continue
      #print 'event....',event
      s.itemclick(event)
      s.sensors(event)
      if event['name'] == 'lrcShow':
        droid.fullSetProperty('lrc', 'text', event['data'])
      if event['name'] == 'click':
        print event
        id = event['data']['id']
        s.listen(id)

Event().start()
