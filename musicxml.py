# -*- coding: utf-8 -*-

__author__ = 'By: ざ凍結の→愛\nQQ: 892768447\nEmail: 892768447@qq.com'

__copyright__ = 'Copyright (c) 2009, ざ凍結の→愛.'

__version__ = 'Version 1.0'

Layout = '''<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent"
    android:background="file:///mnt/sdcard/ZceMusic/images/bg.jpg" >

    <ImageButton
        android:id="@+id/left"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:layout_alignParentLeft="true"
        android:layout_alignParentTop="true"
        android:background="file:///mnt/sdcard/ZceMusic/images/left.png" />

    <ImageButton
        android:id="@+id/exit"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:layout_alignParentRight="true"
        android:layout_alignParentTop="true"
        android:background="file:///mnt/sdcard/ZceMusic/images/exit.png" />

    <ImageView
        android:id="@+id/picture"
        android:layout_width="230dp"
        android:layout_height="164dp"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="70dp"
        android:background="file:///mnt/sdcard/ZceMusic/images/picture.jpg" />

    <TextView
        android:id="@+id/lrc"
        android:layout_width="192dp"
        android:layout_height="86dp"
        android:layout_centerHorizontal="true"
        android:layout_centerVertical="true"
        android:gravity="center"
        android:background="#00000000"
        android:textColor="#00FF00" />

    <TextView
        android:id="@+id/time"
        android:layout_width="192dp"
        android:layout_height="14dp"
        android:layout_centerHorizontal="true"
        android:layout_centerVertical="true"
        android:layout_alignLeft="@+id/lrc"
        android:layout_below="@+id/lrc"
        android:layout_marginTop="7dp"
        android:gravity="center"
        android:text=""
        android:background="#00000000"
        android:textColor="#FFFFFF" />

    <TextView
        android:id="@+id/title"
        android:layout_width="192dp"
        android:layout_height="wrap_content"
        android:layout_alignLeft="@+id/lrc"
        android:layout_centerHorizontal="true"
        android:layout_centerVertical="true"
        android:layout_below="@+id/lrc"
        android:layout_marginTop="33dp"
        android:gravity="center"
        android:background="#00000000"
        android:textColor="#FFFFFF" />

    <LinearLayout
        android:layout_width="192dp"
        android:layout_height="48dp"
        android:layout_alignLeft="@+id/title"
        android:layout_below="@+id/title"
        android:layout_marginTop="34dp"
        android:gravity="center" >

        <ImageButton
            android:id="@+id/play"
            android:layout_width="32dp"
            android:layout_height="32dp"
            android:layout_marginRight="10dp"
            android:background="file:///mnt/sdcard/ZceMusic/images/play.png" />

        <ImageButton
            android:id="@+id/pause"
            android:layout_width="32dp"
            android:layout_height="32dp"
            android:background="file:///mnt/sdcard/ZceMusic/images/pause.png" />

        <ImageButton
            android:id="@+id/stop"
            android:layout_width="32dp"
            android:layout_height="32dp"
            android:layout_marginLeft="10dp"
            android:background="file:///mnt/sdcard/ZceMusic/images/stop.png" />
    </LinearLayout>

    <LinearLayout
        android:layout_width="192dp"
        android:layout_height="48dp"
        android:layout_alignParentBottom="true"
        android:layout_centerHorizontal="true"
        android:gravity="center" >

        <ImageButton
            android:id="@+id/on"
            android:layout_width="32dp"
            android:layout_height="32dp"
            android:layout_marginRight="10dp"
            android:background="file:///mnt/sdcard/ZceMusic/images/on.png" />

        <ImageButton
            android:id="@+id/next"
            android:layout_width="32dp"
            android:layout_height="32dp"
            android:layout_marginRight="5dp"
            android:background="file:///mnt/sdcard/ZceMusic/images/next.png" />

        <ImageButton
            android:id="@+id/rewind"
            android:layout_width="32dp"
            android:layout_height="32dp"
            android:layout_marginLeft="5dp"
            android:background="file:///mnt/sdcard/ZceMusic/images/rewind.png" />

        <ImageButton
            android:id="@+id/forward"
            android:layout_width="32dp"
            android:layout_height="32dp"
            android:layout_marginLeft="10dp"
            android:background="file:///mnt/sdcard/ZceMusic/images/forward.png" />
    </LinearLayout>

</RelativeLayout>'''

if __name__ == '__main__':
  import android
  droid = android.Android()
  droid.fullShow(Layout)
  droid.eventWaitFor('key')
