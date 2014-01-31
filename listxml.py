# -*- coding: utf-8 -*-

__author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'

__copyright__ = 'Copyright (c) 2009, ざ凍結の→愛.'

__version__ = 'Version 1.0'

ListLayout = '''<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:background="file:///mnt/sdcard/ZceMusic/images/bg.jpg" >

    <ImageButton
        android:id="@+id/refresh"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:layout_alignParentLeft="true"
        android:layout_alignParentTop="true"
        android:background="file:///mnt/sdcard/ZceMusic/images/refresh.png" />

    <ImageButton
        android:id="@+id/right"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:layout_alignParentRight="true"
        android:layout_alignParentTop="true"
        android:background="file:///mnt/sdcard/ZceMusic/images/right.png" />

    <ListView
        android:id="@+id/list"
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:layout_alignParentLeft="true"
        android:layout_below="@+id/refresh" >
    </ListView>

    <TextView
        android:text="歌曲列表"
        android:textSize="25sp"
        android:gravity="center"
        android:layout_width="wrap_content"
        android:layout_height="48dp"
        android:layout_alignParentTop="true"
        android:layout_centerHorizontal="true" />

</RelativeLayout>'''

if __name__ == '__main__':
  import android
  droid = android.Android()
  droid.fullShow(ListLayout)
  droid.eventWaitFor('key')
