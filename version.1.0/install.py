# -*- coding: utf-8 -*-

__author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'

__copyright__ = 'Copyright (c) 2009, ざ凍結の→愛.'

__version__ = 'Version 1.0'

import os
from os.path import exists
from os import makedirs
from imagesdata import *

MusicImagesPath = '/mnt/sdcard/ZceMusic/images/'
MusicListPath = '/mnt/sdcard/ZceMusic/music.list'

def install():
  if not exists(MusicImagesPath):
    makedirs(MusicImagesPath)
  if not exists(MusicListPath):
    open(MusicListPath,'wb').write('')
  for i in ImagesData:
    if not exists(MusicImagesPath+i):
      open(MusicImagesPath+i,'wb').write(ImagesData[i].decode('base64'))
