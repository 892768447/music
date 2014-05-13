# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from os.path import exists
from config import ImageZipPath,CurrentPath
from music import Music
import traceback

if exists(ImageZipPath):
    from unzip import unZipRes
    unZipRes()#解压资源

try:
    Music().main()
except:
    f = open(CurrentPath+'bug.txt','wb')
    traceback.print_exc(file=f)
    f.flush()
    f.close()
