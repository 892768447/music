# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

from config import Buttons,Attributes,CurrentPath,MusicListPath,MainXmlPath,IsRandom,MenuKeyValue,BackKeyValue
#从配置文件载入xml界面属性设置文件
from pyevent import Event
#事件监听模块
from scan import Scan
#歌曲自动扫描模块
from play import Play
#导入播放功能模块
from isend import IsEnd
#检测歌曲播放状态
from random import randrange
#产生随机数
from os import remove
from time import sleep

class Music(Event):

    def __init__(s):
        #初始化
        Event.__init__(s)
        s.__scan = Scan(s)
        s.__play = Play(s)
        s.__isend = IsEnd(s)
        s.__PlayState = False#播放状态
        s.__PauseState = False#暂停状态
        s.__MusicListState = False#歌曲列表显示状态
        s.__MusicListDialgState = False#歌曲操作对话框状态
        s.__MusicListDelDialgState = False#对话框状态
        s.__delMethod = None#歌曲删除方式 0表示列表删除 1表示物理删除
        s.music_list = None#歌曲名字列表
        s.music_dict = None#歌曲字典
        s.__select_music = None#从歌曲列表中选择的歌曲
        s.__current_music = 1#当前播放的歌曲id
        s.__thread_list = []#保存所有子线程用于结束程序时清理

    def nameEvent(s,name,data):
        #重写名字事件(自定义事件)
        pass

    def keyEvent(s,key):
        #重写按键事件
        #如果不知道键值可以print key然后通过按键得知对应的键值
        if key == MenuKeyValue:
            #菜单键
            #这里必须有先后判断顺序(删除确认框,操作弹出框,歌曲列表框)
            if s.__MusicListDelDialgState:#如果删除确认框显示
                return#无操作。需要返回键取消
            if s.__MusicListDialgState:#歌曲操作框显示
                return#无操作。需要返回键取消
            if s.__MusicListState:#如果显示了歌曲列表则隐藏
                return
            #未显示歌曲列表框则显示
            s.setProperty('music_list','visibility','visible')
            s.__MusicListState = True
        if key == BackKeyValue:
            #返回键
            #这里必须有先后判断顺序(删除确认框,操作弹出框,歌曲列表框,退出程序)
            if s.__MusicListDelDialgState:#如果删除确认框显示
                s.setProperty('music_list_alert_dialog','visibility','gone')#隐藏
                s.__MusicListDelDialgState = False
                s.__delMethod = None#隐藏删除对话框时需要清除删除方式
                return#一次只能做一个动作
            if s.__MusicListDialgState:#歌曲操作框显示
                s.setProperty('music_list_dialog','visibility','gone')#隐藏
                s.__MusicListDialgState = False
                s.__select_music = None
                return
            if s.__MusicListState:#如果显示了歌曲列表则隐藏
                s.setProperty('music_list','visibility','gone')
                s.__MusicListState = False
                s.__select_music = None
                return
            #再次按下返回键弹出提示框提示是否退出程序
            s.__MusicListDelDialgState = True
            s.setProperty('music_list_alert_dialog','visibility','visible')#显示提示框
            s.setProperty('music_list_alert_dialog_info','text','确定要退出程序吗?')#显示提示框

    def clickEvent(s,id):
        #重写点击事件
        #以下是主界面 播放暂停上下一曲按钮事件
        if id == 'music_main_play_pause_btn':
            #播放按钮
            if not s.music_list:
                s.droid.makeToast('当前播放列表为空\n可能正在扫描歌曲')
                return
            if s.__PlayState:#音乐正在播放此时点击则暂停播放
                if s.__PauseState:#如果歌曲被暂停则继续播放
                    s.__play.goon()
                    s.__isend.goon()
                    s.__PauseState = False
                    s._btnEffect('music_main_play_pause_btn','background',Buttons.get('music_main_play_pause_btn').get('play').get('nor'),Buttons.get('music_main_play_pause_btn').get('play').get('pre'))#播放图片特效
                    s.setProperty('music_main_play_pause_btn','background',Buttons.get('music_main_play_pause_btn').get('pause').get('nor'))#已经播放于是设置图片为暂停图片
                else:
                    s.__play.pause()
                    s.__isend.pause()
                    s.__PauseState = True
                    s._btnEffect('music_main_play_pause_btn','background',Buttons.get('music_main_play_pause_btn').get('pause').get('nor'),Buttons.get('music_main_play_pause_btn').get('pause').get('pre'))#暂停图片特效
                    s.setProperty('music_main_play_pause_btn','background',Buttons.get('music_main_play_pause_btn').get('play').get('nor'))#已经播放于是设置图片为播放图片
            else:#没有播放则随机播放一首歌
                s.__current_music = s._randomMusic(len(s.music_list))
                s.__play.play(s.music_dict.get(s.__current_music)[1])
                s.__isend.goon()
                s.__PlayState = True
                s.setProperty('music_main_music_title','text',s.music_list[s.__current_music])
                s._btnEffect('music_main_play_pause_btn','background',Buttons.get('music_main_play_pause_btn').get('play').get('nor'),Buttons.get('music_main_play_pause_btn').get('play').get('pre'))#播放按钮图片特效
                s.setProperty('music_main_play_pause_btn','background',Buttons.get('music_main_play_pause_btn').get('pause').get('nor'))#已经播放于是设置图片为暂停图片

        if id == 'music_main_pre_btn':
            #上一曲按钮
            if not s.__PlayState:#音乐此时未播放则不进行上一曲
                s.__PlayState = True
            if not s.music_list:#歌曲列表为空
                s.droid.makeToast('当前播放列表为空\n可能正在扫描歌曲')
                return
            #随机播放
            if IsRandom:
                s.__current_music = s._randomMusic(len(s.music_list))
                music = s.music_dict.get(s.__current_music)
                s.setProperty('music_main_music_title','text',music[0])
                s.__play.play(music[1])#播放歌曲
                s.__isend.goon()
                return
            #没有随机播放
            s.__current_music -= 1
            if s.__current_music < 1:
                #防止下标越界原本是0
                #因为0被用于刷新列表功能所以这里改为1
                s.__current_music = s._randomMusic(len(s.music_list))
            music = s.music_dict.get(s.__current_music)
            s.setProperty('music_main_music_title','text',music[0])
            s.__play.play(music[1])#播放歌曲
            s.__isend.goon()
            del music
            s.setProperty('music_main_play_pause_btn','background',Buttons.get('music_main_play_pause_btn').get('pause').get('nor'))
            s._btnEffect('music_main_pre_btn','background',Buttons.get('music_main_pre_btn').get('nor'),Buttons.get('music_main_pre_btn').get('pre'))        
                
        if id == 'music_main_next_btn':
            #下一曲按钮
            if not s.__PlayState:#音乐此时未播放则不进行下一曲
                s.__PlayState = True
            if not s.music_list:#歌曲列表为空
                s.droid.makeToast('当前播放列表为空\n可能正在扫描歌曲')
                return
            #随机播放
            if IsRandom:
                s.__current_music = s._randomMusic(len(s.music_list))
                music = s.music_dict.get(s.__current_music)
                s.setProperty('music_main_music_title','text',music[0])
                s.__play.play(music[1])#播放歌曲
                s.__isend.goon()
                return
            #没有随机播放
            s.__current_music += 1#比如35
            length = len(s.music_list)#比如0-35共36
            if s.__current_music >= length:#防止下标越界
                s.__current_music = s._randomMusic(length)
            music = s.music_dict.get(s.__current_music)
            s.setProperty('music_main_music_title','text',music[0])
            s.__play.play(music[1])#播放歌曲
            s.__isend.goon()
            del music
            s.setProperty('music_main_play_pause_btn','background',Buttons.get('music_main_play_pause_btn').get('pause').get('nor'))
            s._btnEffect('music_main_next_btn','background',Buttons.get('music_main_next_btn').get('nor'),Buttons.get('music_main_next_btn').get('pre'))

        #以下是选择歌曲后弹出框点击事件
        if id == 'music_list_dialog_select_btn':
            #播放选择歌曲
            if s.__select_music >= 0:
                music = s.music_dict.get(s.__select_music)
                s.setProperty('music_main_music_title','text',music[0])
                s.__current_music = s.__select_music
                s.__play.play(music[1])#播放歌曲
                s.__isend.goon()
                s.__PlayState = True
                s.setProperty('music_main_play_pause_btn','background',Buttons.get('music_main_play_pause_btn').get('pause').get('nor'))
                s._btnEffect('music_list_dialog_select_btn','background',Buttons.get('music_list_dialog_select_btn').get('nor'),Buttons.get('music_list_dialog_select_btn').get('pre'))
                del music
                #隐藏自己和歌曲列表
                s.setProperty('music_list_dialog','visibility','gone')#隐藏
                s.__MusicListDialgState = False
                s.setProperty('music_list','visibility','gone')
                s.__MusicListState = False

        if id == 'music_list_dialog_share_btn':
            #分享选择歌曲
            s.droid.makeToast('暂未开发')
            s._btnEffect('music_list_dialog_share_btn','background',Buttons.get('music_list_dialog_share_btn').get('nor'),Buttons.get('music_list_dialog_share_btn').get('pre'))
            s.setProperty('music_list_dialog','visibility','gone')#隐藏
            s.__MusicListDialgState = False

        if id == 'music_list_dialog_dellist_btn':
            #删除选择歌曲
            s.__delMethod = 0#列表删除方式
            s._btnEffect('music_list_dialog_dellist_btn','background',Buttons.get('music_list_dialog_dellist_btn').get('nor'),Buttons.get('music_list_dialog_dellist_btn').get('pre'))
            s.setProperty('music_list_dialog','visibility','gone')#隐藏
            s.__MusicListDialgState = False
            s.__MusicListDelDialgState = True
            s.setProperty('music_list_alert_dialog','visibility','visible')#显示提示框
            s.setProperty('music_list_alert_dialog_info','text','确定要从列表中删除 %s 吗?'%s.music_list[s.__select_music])#显示提示框

        if id == 'music_list_dialog_deldisk_btn':
            #抹消选择歌曲
            s.__delMethod = 1#物理删除方式
            s._btnEffect('music_list_dialog_deldisk_btn','background',Buttons.get('music_list_dialog_deldisk_btn').get('nor'),Buttons.get('music_list_dialog_deldisk_btn').get('pre'))
            #点击后隐藏自己显示 提示确认框
            s.setProperty('music_list_dialog','visibility','gone')#隐藏
            s.__MusicListDialgState = False
            s.__MusicListDelDialgState = True
            s.setProperty('music_list_alert_dialog','visibility','visible')#显示提示框
            s.setProperty('music_list_alert_dialog_info','text','确定要从磁盘上删除 %s 吗?'%s.music_list[s.__select_music])#显示提示框

        #以下是弹出确认删除框按钮事件

        if id == 'music_list_alert_dialog_ok_btn':
            #确认删除
            s._btnEffect('music_list_alert_dialog_ok_btn','background',Buttons.get('music_list_alert_dialog_ok_btn').get('nor'),Buttons.get('music_list_alert_dialog_ok_btn').get('pre'))
            print s.__select_music
            if s.__select_music == None:
                for thread in s.__thread_list:
                    print thread
                    thread.stop()
                #exit()
            if s.__delMethod == 0:
                try:
                    #删除选中歌曲
                    s.droid.makeToast('已删除 ' + s.music_list.pop(s.__select_music))#从列表中删除掉
                    s.music_dict.pop(s.__select_music)#这里需要注意从列表中删除第2个元素后列表的对应字典的位置变了,需要把字典做处理
                    for index in range(s.__select_music+1,len(s.music_list)+1):
                        s.music_dict[index-1] = s.music_dict.get(index)#一次把删除id后面的id数字减1
                    s.music_dict.pop(index)
                    s.setList('music_list_list',s.music_list)#设置歌曲列表
                    open(MusicListPath,'wb').write(str(s.music_dict))
                except Exception,e:
                    print e
                s.setProperty('music_list_alert_dialog','visibility','gone')#隐藏
                s.__MusicListDialgState = False
                s.__MusicListDelDialgState = False
                return
            if s.__delMethod == 1:
                try:
                    #删除选中歌曲
                    s.droid.makeToast('已删除 ' + s.music_list.pop(s.__select_music))#从列表中删除掉
                    music = s.music_dict.pop(s.__select_music)#删除字典中的元素返回该删除值
                    remove(music[1])#物理删除文件
                    for index in range(s.__select_music+1,len(s.music_list)+1):
                        s.music_dict[index-1] = s.music_dict.get(index)#一次把删除id后面的id数字减1
                    s.music_dict.pop(index)
                    s.setList('music_list_list',s.music_list)#设置歌曲列表
                    open(MusicListPath,'wb').write(str(s.music_dict))
                except Exception,e:
                    print e
                s.setProperty('music_list_alert_dialog','visibility','gone')#隐藏
                s.__MusicListDialgState = False
                s.__MusicListDelDialgState = False
                return

        if id == 'music_list_alert_dialog_cancle_btn':
            #取消
            s._btnEffect('music_list_alert_dialog_cancle_btn','background',Buttons.get('music_list_alert_dialog_cancle_btn').get('nor'),Buttons.get('music_list_alert_dialog_cancle_btn').get('pre'))
            s.__delMethod = None
            s.setProperty('music_list_alert_dialog','visibility','gone')#隐藏
            s.__MusicListDelDialgState = False

    def itemClickEvent(s,id,position):
        #重新列表单击事件
        if id == 'music_list_list':
            #点击歌曲列表
            if s.__MusicListDelDialgState:#如果删除提示框存在则不做任何操作
                return
            if position == 0:#选择了刷新歌曲
                s.setList('music_list_list',['刷新歌曲列表'])
                scan = Scan(s)
                scan.delete()
                scan.start()
                s.droid.makeToast('正在扫描歌曲')
                s.__thread_list.append(scan)
                s._setMusicList()#加载缓存歌曲列表
                return
            if not s.__MusicListDialgState:#歌曲操作框没有显示
                s.__select_music = position
                s.setProperty('music_list_dialog','visibility','visible')#显示
                s.setProperty('music_list_dialog_title','text',s.music_list[position])#设置操作框标题
                s.__MusicListDialgState = True
                return
            #否则不采取动作一直显示之前操作框。保证无论点击什么歌曲都只有第一次有效

    def autoNext(s):
        #当一首歌播放完毕时自动下一曲
        if not s.music_list:#歌曲列表为空
            s.droid.makeToast('当前播放列表为空\n可能正在扫描歌曲')
            return
        #随机播放
        if IsRandom:
            s.__current_music = s._randomMusic(len(s.music_list))
            music = s.music_dict.get(s.__current_music)
            s.setProperty('music_main_music_title','text',music[0])
            s.__play.play(music[1])#播放歌曲
            s.__isend.goon()
            return
        #没有随机播放
        s.__current_music += 1#比如35
        length = len(s.music_list)#比如0-35共36
        if s.__current_music >= length:
            #防止下标越界
            s.__current_music = s._randomMusic(length)
        music = s.music_dict.get(s.__current_music)
        s.setProperty('music_main_music_title','text',music[0])
        s.__play.play(music[1])#播放歌曲
        s.__isend.goon()
        del music
    
    def _setAttr(s):
        for aid in Attributes.keys():#从属性值中获取所有id
            Propertys = Attributes.get(aid)#根据id获取所有属性
            if Propertys:#如果存在
                for pro in Propertys.keys():#获取所有属性名
                    s.setProperty(aid,pro,Propertys.get(pro))#根据属性名获取属性值

    def _setMusicList(s):
        try:
            s.music_dict = open(MusicListPath,'rb').read()
            s.music_dict = eval(s.music_dict)#{0:('name','path')}
            s.music_list = [s.music_dict.get(key)[0] for key in s.music_dict.keys()]
            #把所有歌名存到一个列表中
            s.setList('music_list_list',s.music_list)#设置歌曲列表
        except IOError,e:
            print e
        except Exception,e:
            print e

    def _randomMusic(s,length):
        Id = randrange(length)
        #随机产生的数据不为0
        #根据歌曲个数随机产生一个数字作为索引从而得到列表中的歌曲名字和地址
        return Id if(Id != 0) else s._randomMusic(length)

    def _btnEffect(s,id,pro,value1,value2):#按钮点击时的特效
        s.setProperty(id,pro,value2)
        sleep(0.1)
        s.setProperty(id,pro,value1)
        sleep(0.1)

    def main(s):
        #运行
        try:
            main_xml = open(MainXmlPath,'rb').read().replace('IMAGES',CurrentPath + 'images')
        except IOError,e:
            print e
            s.droid.makeToast(str(e))
            #exit()
        s.setXml(main_xml,'zmusic')
        s.show()#显示界面
        #s.start()#启动事件监听
        s._setAttr()#设置属性
        s._setMusicList()#加载缓存歌曲列表
        s.__scan.start()#开始自动后台扫描歌曲
        s.__isend.start()
        s.__thread_list.append(s.__scan)
        s.__thread_list.append(s.__play)
        s.__thread_list.append(s.__isend)
        s.__thread_list.append(s)
        s.run()#非子线程启动事件监听
