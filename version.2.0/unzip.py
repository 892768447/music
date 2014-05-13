# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from zipfile import ZipFile
#from os import remove
from config import ImageZipPath,ImagesPath

def unZipRes():
    try:#解压图片资源到目录
        fp = ZipFile(ImageZipPath,'r')
        for f in fp.namelist():
            fp.extract(f,ImagesPath)
        #remove(ImageZipPath)
    except Exception,e:
        print e
