# -*- coding: UTF-8 -*-
import os
import datetime
import time

import subprocess
import sys
# from  modules.app import  *
#
import re

import time

# with open("C:\\Users\\root\\Desktop\\activity_info.log", "a+") as f:
#     # ^ Package:.*
#
#     lines = f.readlines()
#     components = []
#     for line in lines:
#         le = line.replace(" ", "").replace("\n", "")
#         if le.startswith("Package:"):
#             package = le.replace("Package:","")
#             print package
#             continue
#         if not le.startswith("Permission"):
#             if not (le.startswith("TargetActivity:") or le.startswith("ParentActivity:")):
#                 components.append(le)
#         else:
#             continue
line = "com.huawei.camerakit.impl (HwCameraKit)"
app_name = line[line.rfind('('):line.rfind(')')].replace("(","").replace(")","")
print app_name


    # print connect
    # mc = re.match(r"\s\s\S.*\s.*\s.*Permission: null")
    # print mc.group(0)

    # comp = re.compile(r"^\s\s\S.*\s.*\s.*Permission: null")
    # comp = re.findall("(\W*)\W*Permission: null",connect)
    # comp =  re.findall(r"([\S\.]*)\W.*\W*Permission: null",connect)
    # for c in comp:
    #     print c
    # print comp

    # conts = comp.findall(connect)
    # for cont in conts:
    #     print str(cont).replace("Permission: null","")

    # comp = re.match(r'.*\r\nPermission: null', connect)
    # print aa

    # print connect

# AttackSurface("")
#
# connect =  os.popen("adb connect 192.168.43.1")
# print connect.read()
# forward =  os.popen("adb forward tcp:41415 tcp:41415")
# print forward.read()
#
#
#
# with open("C:\Users\\root\Desktop\info.log","w+") as f:
#     p = subprocess.Popen("drozer console connect --server 192.168.43.1:41415", shell=True, stdin=subprocess.PIPE,stdout=f.fileno(), stderr=subprocess.PIPE)
#     resl = f.readline()
#     print resl
#     p.stdin.write("run app.package.list  \n".encode("utf-8"))
#     p.stdin.flush()
#
#     # !/usr/bin/python
#     # -*- coding: UTF-8 -*-
#     import os
#     import sys
#
#     f = open("help.txt", 'w')  # 创建文件对象
#     sys.stdout_backup = sys.stdout  # 先把默认的输出地址备份
#     sys.stdout = f  # 把输出地址改成f文件对象，下面所有内容都将出现在txt文档里
#     sys.stdout = sys.stdout_backup  # 把stdout的输出地址再改回来
#
#


# forward = "adb forward tcp:41415 tcp:41415"

# print("xxxxxxxxxxxxxxxxxx")
# # drozer console connect --server 192.168.43.1:41415
#
# print p.pid
#
# # print(p.stdout.read())
# p.stdin.write("run app.package.list  \n".encode("utf-8"))
# p.stdin.flush()
# out,err = p.communicate()
# print out,err
#
# p.stdin.write("exit()  \n".encode("utf-8"))
# p.stdin.flush()
# # p.wait()
# # p.stdin.write(bytes('print(2) \n'),'utf-8')
# # p.stdin.write(bytes('print(3) \n'),'utf-8')
# out,err = p.communicate()
# print out,err

# subprocess.Popen.communicate(input=None, timeout=None)
# result = p.stdout.readlines()
# for re in result:
#     print(re)
# print("xxxxxxx")
# print("====",result)
# p.stdin.write(bytes("list",'utf-8'))
# p.stdin.write(bytes("\n",'utf-8'))
# p.stdin.flush()
# result = p.stdout.readlines()
# print(result)

# res = subprocess.Popen('drozer console connect  --server 127.0.0.1:41415',shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=False)
# list_cmd = "run app.package.list"
# print(res.pid)
# result = res.stdout.readlines()
# print(result)l
# res.stdin.write(bytes(list_cmd,'utf-8'))
# res.stdin.write(bytes("\n",'utf-8'))
# res.stdin.flush()
# result = res.stdout.readlines()
# print(result)

# p = subprocess.Popen("cmd.exe",shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
# p.stdin.write("echo Hello!".encode("GBK"))
# p.stdin.flush()
# result = p.stdout.readlines()
# print(result)

# res = subprocess.run(['drozer', 'console', 'connect',  '--server', '127.0.0.1:41415'],shell=True,stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
# result = res.stdout.readlines()
# print(result)



temp_root_path ="C:\\Users\\root\\Desktop\\"
pa = os.path.join(temp_root_path, "embedded_ca")
file = open(pa, "w+")
print  os.path.getsize(pa)
