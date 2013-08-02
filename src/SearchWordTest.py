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
    device.installPackage('d:/有道词典V4.0.3.apk'.decode('utf-8'))
    log.write("安装apk包...\n")
    print("The apk has installed successfully")
    device.startActivity(component='com.youdao.dict/.activity.DictSplashActivity')
    log.write("启动有道词典\n")
    #等待app启动完毕
    mr.sleep(5)
    
    log.write("点击接受按钮，接受用户服务条款\n")
    device.touch(500, 1200,"DOWN_AND_UP");
    mr.sleep(2)
    
    log.write("现在页面展示的是PPT页面，需要向左滑动\n")
    #参数分别为初始点和结束点，持续时间和步数
    for i in range(1, 4):
        log.write("向左滑动\n")
        device.drag((550,500),(100,500), 0.5, 1)
        mr.sleep(2)
        
    log.write("取消安装有道云笔记的checkbox\n")
    device.touch(80, 1050, "DOWN_AND_UP")
    
    log.write("点击立即体验按钮，进入程序主页面\n")
    device.touch(400, 800, "DOWN_AND_UP")
    
    log.write("等待主页面加载完毕\n")
    mr.sleep(3)
    
    
    log.write("点击单词输入框\n")
    device.touch(200, 700, "DOWN_AND_UP")
    mr.sleep(1)
    
    log.write("输入单词linux\n")
    device.type("linux")
    print("type the word 'linux'")
    
    log.write("点击搜索按钮\n")
    device.touch(680, 100, "DOWN_AND_UP")
    mr.sleep(5)
    
    log.write("截图保存到"+screenShotPath+"\n")
    print("Take a picture")
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    mainPageImage = device.takeSnapshot()
    
    imageTrue = mr.loadImageFromFile('d:/shot/true.png')
    if(imageTrue.sameAs(mainPageImage, 0.75)):
        log.write('截图比较成功\n')
    else:
        log.write('截图比较失败\n')
    mainPageImage.writeToFile(screenShotPath+"主页面截图".decode("utf-8")+now+".png", "png")
    
    log.write("向上滑动，查看结果\n")
    for i in range(1, 4):
        device.drag((300,100), (300, 800), 0.5, 1);
        mr.sleep(1)
        
    for i in range(1, 4):
        log.write("点击手机的后退按钮\n")
        device.press("KEYCODE_BACK", "DOWN_AND_UP")
        mr.sleep(2)
    log.close()
    #device.removePackage('com.youdao.dict')
    print("The package has removed successfully!")
    print(filename+" over!\n\n")
if __name__ == '__main__':
    main()