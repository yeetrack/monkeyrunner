#!/usr/bin/env monkeyrunner
# coding=utf-8
# Copyright 2010, The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import time
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer

def main():
    screenShotPath = "d:/python/screenshots/"
    #输出日志
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    logPath = "d:/python/log/"
    
    names = sys.argv[0].split('\\')
    filename = names[len(names)-1]
    print("++++++++++++++++++++++++++++++++++++++")
    print("Start execute "+filename)
    filename.replace('.py', '')
    log = open(logPath+filename[:-3]+"-log-"+now+".txt", "w")
    device = mr.waitForConnection(30,'021YLJ4C35002735')
    log.write("等待手机连接...、\n")
    
    device.startActivity(component='com.youdao.dict/.activity.DictSplashActivity')
    log.write("启动有道词典\n")
    #等待app启动完毕
    mr.sleep(5)
    
    log.write("点击翻译标签页")
    device.touch(250, 100, "DOWN_AND_UP")
    mr.sleep(1)
    
    log.write("点击翻译输入框")
    device.touch(300, 500, "DOWN_AND_UP")
    mr.sleep(2)
    
    log.write("monkeyrunner无法输入中文，只能输入ascii字符\n")
    device.type("Hello")
    device.press("KEYCODE_SPACE", "DOWN_AND_UP")
    device.type("world")
    print("input 'hello world'")
    mr.sleep(2)
    log.write("点击搜索按钮")
    print('enter the search button')
    device.touch(500, 200, "DOWN_AND_UP")
    log.write("等待查询结果")
    mr.sleep(5)
    
    log.write("对查询结果截图")
    resultImage = device.takeSnapshot()
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    resultImage.writeToFile(screenShotPath+filename+"-翻译语句截图".decode("utf-8")+now+".png", "png")
    print("Take a picture")
    
    for i in range(1, 4):
        log.write("点击手机的后退按钮\n")
        device.press("KEYCODE_BACK", "DOWN_AND_UP")
        mr.sleep(2)
    
    log.close()
    
    print(filename+" over!\n\n")
if __name__ == '__main__':
    main()