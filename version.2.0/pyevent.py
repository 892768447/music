# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 4.0'

from threading import _sleep,Thread,Timer
from os.path import dirname
#from os import abort
from android import Android

class _Loop(Thread):
    def __init__(s,target=None,args=(),kwargs={}):
        Thread.__init__(s)
        s.setDaemon(True)
        s.__running = False
        s.__target = target
        s.__args = args
        s.__kwargs = kwargs

    def stop(s):
        s.__running = False

    def run(s):
        while s.__running:
            if not s.__running:
                break
            try:
                if s.__target:
                    s.__target(*self.__args,**self.__kwargs)
            finally:
                del s.__target,self.__args,self.__kwargs
            s.__running = False
            break

#class Event(Thread):
class Event(object):

    def __init__(s):
        #Thread.__init__(s)
        s.droid = Android()
        s.__cxml = None#当前xml
        s.__ctitle = ''
        s.__running = False

    def setXml(s,xml,title=''):
        s.__cxml = str(xml)
        s.__ctitle = str(title)

    def loop(s,target=None,args=(),kwargs={}):
        if not target:
            return
        l = _Loop(target=target,args=args,kwargs=kwargs)
        return l
    
    def timer(interval,function,args=[],kwargs={}):
        t = Timer(interval,function,args=[],kwargs={})
        t.setDaemon(True)
        return t

    def show(s):
        try:
            s.droid.fullShow(s.__cxml,s.__ctitle)
        except Exception,e:
            pass

    def hide(s):
        try:
            s.droid.fullDismiss()
        except Exception,e:
            pass

    def stop(s):
        s.__running = False
        try:
            s.droid.fullDismiss()
        except Exception,e:
            pass

    def run(s):
        s.__running = True
        while s.__running:
            if not s.__running:
                break
            _sleep(0.1)
            try:
                result = s.droid.eventPoll(1).result
            except Exception,e:
                result = None
                pass
            if result == True or result == False or result == 'OK' or result == None:continue
            if not result:continue
            try:
                result = result[0]
                name = result['name']
                data = result['data']
            except Exception,e:
                name = None
                data = None
            s.nameEvent(name,data)
            if name == 'click':
                id = data.get('id')
                s.clickEvent(id)
            if name == 'itemclick':
                id = data.get('id')
                position = int(data.get('position'))
                s.itemClickEvent(id,position)
            if name == 'key':
                key = data.get('key')
                s.keyEvent(key)

    def setProperty(s,id,property,value):
        try:
            s.droid.fullSetProperty(id,property,value)
        except Exception,e:
            pass

    def setList(s,id,list):
        try:
            s.droid.fullSetList(id,list)
        except Exception,e:
            pass

    def queryDetail(s,id,property):
        try:
            return s.droid.fullQueryDetail(id).result.get(property)
        except Exception,e:
            pass
            return None

    def queryAll(s):
        try:
            return s.droid.fullQuery()
        except Exception,e:
            pass
            return {}

    def nameEvent(s,name,data):
        pass

    def clickEvent(s,id):
        pass

    def itemClickEvent(s,id,position):
        pass

    def keyEvent(s,key):
        pass
