# -*- coding: utf-8 -*-

__Author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'
__Copyright__ = 'Copyright (c) 2014 ざ凍結の→愛'
__Version__ = 'Version 2.0'

import os
import sys
CurrentPath = os.path.dirname(sys.argv[0]) + '/'#获取当前脚本所在目录
del os,sys

ScanPath = '/mnt/sdcard/'#歌曲扫描路径
MainXmlPath = '%smain.xml'%CurrentPath#主界面文件
MusicListPath = '%smusic.list'%CurrentPath#歌曲列表缓存文件
ImageZipPath = '%simages.zip'%CurrentPath#图片资源文件
LoadingPath = '%simages/loading/'%CurrentPath#扫描进度条图片资源路径
LoadingTotal = ('sound_hound_loading_%s.png',4)#图片数量按数字排序好
DiscPath = '%simages/disc/'%CurrentPath#圆碟资源路径
DiscTotal = ('disc_extern_%s.png',24)#
ImagesPath = '%simages/'%CurrentPath#/data/data/xx.xxx.xx/files/images/
ProgressBarLength = 40#进度条总长度也就是_*40这个和屏幕大小有关

ExtList = ('.mp3','.ogg','.wav')#扫描歌曲的后缀
MusicSize = 1 * 1024 * 1024#大于1M的歌曲才添加
MusicSearchUrl = 'http://shopcgi.qqmusic.qq.com/fcgi-bin/shopsearch.fcg?value=%s&artist=%s&page_record_num=10'
#歌曲搜索链接 其中两个格式化输入 value=%s  artist=%s  对应 歌曲名字和歌手
MusicLrcUrl = 'http://music.qq.com/miniportal/static/lyric/%s/%s.xml'
#歌词下载链接 其中两个格式化输入

MenuKeyValue = '82'#菜单键键值
BackKeyValue = '4'#返回键键值

AutoDownLrc = True#是否自动下载歌词
IsRandom = True#是否随机播放

#按钮特效使用
Buttons = {
    #上一曲按钮两个图片地址
    'music_main_pre_btn':{'nor':'file://%simages/main/clip_pre_pressed.png'%CurrentPath,'pre':'file://%simages/main/clip_pre_normal.png'%CurrentPath},
    #下一曲按钮两个图片地址
    'music_main_next_btn':{'nor':'file://%simages/main/clip_next_pressed.png'%CurrentPath,'pre':'file://%simages/main/clip_next_normal.png'%CurrentPath},
    #播放暂停按钮图片地址(注意有两个,一个是play一个是pause)
    'music_main_play_pause_btn':{'play':{'nor':'file://%simages/main/clip_play_pressed.png'%CurrentPath,'pre':'file://%simages/main/clip_play_normal.png'%CurrentPath},'pause':{'nor':'file://%simages/main/clip_pause_pressed.png'%CurrentPath,'pre':'file://%simages/main/clip_pause_normal.png'%CurrentPath}},

    #弹出框选择播放按钮
    'music_list_dialog_select_btn':{'nor':'file://%simages/dialog/effect_dolby_icon_press.png'%CurrentPath,'pre':'file://%simages/main/effect_dolby_icon_normal.png'%CurrentPath},
    #弹出框分享按钮
    'music_list_dialog_share_btn':{'nor':'file://%simages/dialog/effect_dolby_icon_press.png'%CurrentPath,'pre':'file://%simages/main/effect_dolby_icon_normal.png'%CurrentPath},
    #弹出框从列表删除按钮
    'music_list_dialog_dellist_btn':{'nor':'file://%simages/dialog/effect_dolby_icon_press.png'%CurrentPath,'pre':'file://%simages/main/effect_dolby_icon_normal.png'%CurrentPath},
    #弹出框从磁盘删除按钮
    'music_list_dialog_deldisk_btn':{'nor':'file://%simages/dialog/effect_dolby_icon_press.png'%CurrentPath,'pre':'file://%simages/main/effect_dolby_icon_normal.png'%CurrentPath},

    #弹出框 确定按钮
    'music_list_alert_dialog_ok_btn':{'nor':'file://%simages/dialog/effect_none_icon_press.png'%CurrentPath,'pre':'file://%simages/main/effect_none_icon_normal.png'%CurrentPath},
    #弹出框 取消按钮
    'music_list_alert_dialog_cancle_btn':{'nor':'file://%simages/dialog/effect_dirac_icon_press.png'%CurrentPath,'pre':'file://%simages/main/effect_dirac_icon_normal.png'%CurrentPath}
}

Attributes = {
    #id为music_main 主界面背景图片地址
    'music_main':{'background':'file://%simages/main/sound_hound_album_back.png'%CurrentPath},
    #id为music_main_play_time 主界面中歌曲已播放时间,可以添加颜色属性等等
    'music_main_play_time':{'textColor':'#FFFFFF','text':'00:00'},
    #id为music_main_end_time 主界面中歌曲总时间,可以添加颜色属性等等
    'music_main_end_time':{'textColor':'#FFFFFF','text':'00:00'},
    #id为music_main_progressBar 播放进度属性
    'music_main_progressBar':{'maxLength':'100','text':'','textColor':'#FFFFFF'},
    #id为music_main_pre_btn 上一曲按钮
    'music_main_pre_btn':{'background':'file://%simages/main/clip_pre_pressed.png'%CurrentPath},
    #id为music_main_play_pause_btn 播放暂停按钮
    'music_main_play_pause_btn':{'background':'file://%simages/main/clip_play_pressed.png'%CurrentPath},
    #id为music_main_next_btn 下一曲按钮
    'music_main_next_btn':{'background':'file://%simages/main/clip_next_pressed.png'%CurrentPath},
    #id为music_main_left_horn 左边喇叭图片
    'music_main_left_horn':{'src':'file://%simages/main/playview_scrap_left.png'%CurrentPath},
    #id为music_main_rigth_horn 右边喇叭图片
    'music_main_rigth_horn':{'src':'file://%simages/main/playview_scrap_rigth.png'%CurrentPath},
    #id为music_main_music_title 主界面歌词标题
    'music_main_music_title':{'text':'','textColor':'#FFFFFF'},
    #id为music_main_lrc_text3 主界面歌词显示框3
    'music_main_lrc_text3':{'text':'','textColor':'#999999'},
    #id为music_main_lrc_text2 主界面歌词显示框2
    'music_main_lrc_text2':{'text':'','textColor':'#999999'},
    #id为music_main_lrc_text1 主界面歌词显示框1
    'music_main_lrc_text1':{'text':'','textColor':'#FFFFFF'},
    #id为music_main_disc_extern 主界面中心圆碟
    'music_main_disc_extern':{'src':'file://%simages/disc/disc_extern_0.png'%CurrentPath},

    #id为music_list 歌曲列表界面(默认隐藏)
    'music_list':{'background':'#a0000000','visibility':'gone'},
    #id为music_list_loading 扫描歌曲时的进度条
    'music_list_loading':{'src':'file://%simages/loading/sound_hound_loading_0.png'%CurrentPath,'visibility':'gone'},
    #id为music_list_list 歌曲列表
    'music_list_list':{'textColor':'#FFFFFF'},

    #id为music_list_dialog 为歌曲选中后的操作弹出框(默认隐藏)
    'music_list_dialog':{'background':'#00000000','gravity':'center','visibility':'gone'},
    #id为music_list_dialog_bg 为歌曲选择后弹出框背景
    'music_list_dialog_bg':{'background':'file://%simages/dialog/dialog_bg.png'%CurrentPath},
    #id为music_list_dialog_title 选择歌曲 标题
    'music_list_dialog_title':{'gravity':'center','text':'','textColor':'#FFFFFF'},
    #id为music_list_dialog_select_icon 选择播放图标
    'music_list_dialog_select_icon':{'layout_width':'48dp','layout_height':'48dp','src':'file://%simages/dialog/from_list_play_pressed.png'%CurrentPath},
    #id为music_list_dialog_select_text 选择播放的文字提示
    'music_list_dialog_select_text':{'gravity':'center','text':'播放选择歌曲','textColor':'#FFFFFF'},
    #id为music_list_dialog_select_btn 选择播放按钮
    'music_list_dialog_select_btn':{'layout_width':'72dp','layout_height':'48dp','background':'file://%simages/dialog/effect_dolby_icon_press.png'%CurrentPath},
    #id为music_list_dialog_share_icon 选择分享图标
    'music_list_dialog_share_icon':{'layout_width':'48dp','layout_height':'48dp','src':'file://%simages/dialog/sound_hound_share_press.png'%CurrentPath},
    #id为music_list_dialog_share_text 选择分享的文字提示
    'music_list_dialog_share_text':{
'gravity':'center','text':'分享选择歌曲','textColor':'#FFFFFF'},
    #id为music_list_dialog_share_btn 选择分享按钮
    'music_list_dialog_share_btn':{'layout_width':'72dp','layout_height':'48dp','background':'file://%simages/dialog/effect_dolby_icon_press.png'%CurrentPath},
    #id为music_list_dialog_dellist_icon 选择删除图标
    'music_list_dialog_dellist_icon':{'layout_width':'48dp','layout_height':'48dp','src':'file://%simages/dialog/list_item_delete_pressed.png'%CurrentPath},
    #id为music_list_dialog_dellist_text 选择删除的文字提示
    'music_list_dialog_dellist_text':{'gravity':'center','text':'删除选择歌曲','textColor':'#FFFFFF'},
    #id为music_list_dialog_dellist_btn 选择删除按钮
    'music_list_dialog_dellist_btn':{'layout_width':'72dp','layout_height':'48dp','background':'file://%simages/dialog/effect_dolby_icon_press.png'%CurrentPath},
    #id为music_list_dialog_deldisk_icon 选择删除2图标
    'music_list_dialog_deldisk_icon':{'layout_width':'48dp','layout_height':'48dp','src':'file://%simages/dialog/list_item_delete_pressed.png'%CurrentPath},
    #id为music_list_dialog_deldisk_text 选择删除2的文字提示
    'music_list_dialog_deldisk_text':{'gravity':'center','text':'抹消选择歌曲','textColor':'#FFFFFF'},
    #id为music_list_dialog_deldisk_btn 选择删除2按钮
    'music_list_dialog_deldisk_btn':{'layout_width':'72dp','layout_height':'48dp','background':'file://%simages/dialog/effect_dolby_icon_press.png'%CurrentPath},

    #id为music_list_alert_dialog 删除确认框(默认隐藏)
    'music_list_alert_dialog':{'background':'#00000000','gravity':'center','visibility':'gone'},
    #id为music_list_alert_dialog_bg 删除确认框背景
    'music_list_alert_dialog_bg':{'background':'file://%simages/dialog/dialog_bg.png'%CurrentPath},
    #id为music_list_alert_dialog_titile_icon 确认框标题图标
    'music_list_alert_dialog_titile_icon':{'layout_width':'48dp','layout_height':'48dp','src':'file://%simages/dialog/list_item_details_pressed.png'%CurrentPath},
    #id为music_list_alert_dialog_titile_text 确认框标题
    'music_list_alert_dialog_titile_text':{'layout_width':'72dp','text':'提示','textColor':'#FFFFFF'},
    #id为music_list_alert_dialog_info 确认框提示内容
    'music_list_alert_dialog_info':{'layout_height':'48dp','gravity':'center','text':'确定要删除吗?','textColor':'#FFFFFF'},
    #id为music_list_alert_dialog_ok_btn 确认框确定按钮
    'music_list_alert_dialog_ok_btn':{'layout_width':'72dp','layout_height':'48dp','text':'确定','textColor':'#FFFFFF','background':'file://%simages/dialog/effect_none_icon_press.png'%CurrentPath},
    #id为music_list_alert_dialog_cancle_btn 确认框取消按钮
    'music_list_alert_dialog_cancle_btn':{'layout_width':'72dp','layout_height':'48dp','text':'取消','textColor':'#FFFFFF','background':'file://%simages/dialog/effect_dirac_icon_press.png'%CurrentPath},
}
