# -*- coding: UTF-8 -*-
import os
import time
from drozer.console.session import Session
from drozer.connector import ServerConnector

# Drozer配置文件
class Arguments():
    def __init__(self, ipAdrr):
        self.server = ipAdrr

    accept_certificate = False
    command = "connect"
    debug = False
    device = None
    file = []
    no_color = False
    onecmd = None
    password = False
    ssl = False


class Fuzz():
    def __init__(self, ipAdrr):
        arguments = Arguments(ipAdrr)
        server = ServerConnector(arguments, None)
        devices = server.listDevices().system_response.devices
        device = devices[0].id
        response = server.startSession(device, None)
        session_id = response.system_response.session_id
        self.session = Session(server, session_id, arguments)

    def get_packages(self, temp_root_path):
        package_path = os.path.join(temp_root_path, "package")
        if not os.path.exists(package_path):
            package_file = open(package_path, "w+")
            self.session.stdout = package_file
            cmd = "app.package.list"
            self.session.do_run(cmd)
            time.sleep(2)
            package_file.close()

        with open(package_path, "r") as package_file:
            for line in package_file:
                package_name = line[:line.rfind(' (')]
                app_name = line[line.rfind('('):line.rfind(')')].replace("(", "").replace(")", "")
                components_types = ["activity", "service", "broadcast", "provider"]
                for components_type in components_types:
                    self.getComponentsInfo(temp_root_path, package_name, app_name, components_type)
                    time.sleep(5)

            package_file.close()

    def getComponentsInfo(self, temp_root_path,package_name,app_name, components_type):
        components_info_path = os.path.join(temp_root_path, package_name+"_"+components_type+"_info")
        if not os.path.exists(components_info_path):
            components_info_file = open(components_info_path, "w+")
            self.session.stdout = components_info_file
            cmd = "app.%s.info -a %s" % (components_type,package_name)
            print cmd
            self.session.do_run(cmd)
            time.sleep(2)
            components_info_file.close()
        modules = []
        components_names = self.getComponents(components_info_path,components_type,app_name)
        for components_name in components_names:
            print "====== components_name is:"+components_name
            if components_type == "activity":
                modules = ["start"]
            elif components_type == "service":
                modules = ["start", "stop"]
            elif components_type == "broadcast":
                pass
                # self.clStr(components_names, le)
            elif components_type == "provider":
                pass
                # self.pclStr(components_names, le)
            self.startComponents(components_type, modules, package_name, components_name)
            # self.startComponents(components_type,package_name,components_name)

    # 对组件进行操作并进行截图
    def startComponents(self,components_type,modules,package_name,components_name):
        for module in modules:
            print components_name +" runing "+components_type+module+"..."
            cmd = "app.%s.%s --component %s %s" % (components_type,module,str(package_name), str(components_name))
            print cmd
            self.session.do_run(cmd)
            time.sleep(5)
            print "screencaping ...."
            screencap_cmd = "adb shell screencap -p /sdcard/tempimg/%s_%s.png" % (str(package_name),str(components_name))
            os.popen(screencap_cmd)
            os.popen("adb shell am start com.mwr.dz/com.mwr.dz.activities.MainActivity")

    # 停止组件并进行截图
    def stopComponents(self,components_type,package_name,components_name):
        cmd = "app.%s.stop --component %s %s" % (components_type, str(package_name), str(components_name))
        print cmd
        self.session.do_run(cmd)
        time.sleep(5)
        screencap_cmd = "adb shell screencap -p /sdcard/tempimg/%s_%s.png" % (str(package_name),str(components_name))
        os.popen(screencap_cmd)
        os.popen("adb shell am start com.mwr.dz/com.mwr.dz.activities.MainActivity")

    def getComponents(self, components_info_path, components_type,app_name):
        print components_type
        components_names = []

        # 忽略0kb大小的文件
        if os.path.getsize(components_info_path) == 0:
            return components_names

        with open(components_info_path) as components_info_file:
            for line in components_info_file:
                le = line.replace(" ", "").replace("\n", "")
                # 忽略第一行的包信息
                if le.startswith("Package:"):
                    package = le.replace("Package:", "")
                    print "====== this package is:" + str(package) +"_"+ str(app_name)
                    continue

                # 忽略没有组件导出的文件
                if le.startswith("Noexportedservices.") or le.startswith("Nomatchingreceivers.") or le.startswith("Nomatchingactivities.") or le.startswith("Nomatchingproviders."):
                    print "no exported...."
                    return components_names

                if components_type == "activity":
                    self.clStr(components_names,le)
                elif components_type == "service":
                    self.clStr(components_names,le)
                elif components_type== "broadcast":
                    self.clStr(components_names,le)
                elif components_type == "provider":
                    self.pclStr(components_names,le)
                else:
                    break
            return components_names

    def clStr(self,components_names,le):
        print le
        # 忽略所有Permission行
        if not le.startswith("Permission"):
            print "no Permission...."
            if not (le.startswith("ParentActivity:") or le.startswith("TargetActivity:")):
                if len(le)>0:
                    print "====== add components_name to components_names:"+le
                    components_names.append(le)
            else:
                print "is ParentActivity  and TargetActivity...."
        else:
            permission_package = le.replace("Permission:", "")
            if not permission_package.startswith("null"):
                print "permission no is null ...."
                if len(components_names)!=0:
                    print "====== remove components_name to components_names:" + components_names[len(components_names)-1]
                    components_names.remove(components_names[len(components_names)-1])

    def pclStr(self,components_names,le):
        pass

if __name__ == '__main__':

    temp_root_path = "C:\\Users\\root\\Desktop\\temp"
    if False:
        ip = "192.168.43.1"
        port = "41415"
        ipAdrr = "%s:%s" % (ip, port)

        connect_cmd = "adb connect %s" % ip
        forward_cmd = "adb forward tcp:%s tcp:%s" % (port, port)
        rm_img_cmd = "adb shell rm -rf /sdcard/tempimg/"

        connect = os.popen(connect_cmd)
        forward = os.popen(forward_cmd)
        forward = os.popen(rm_img_cmd)
    else:
        ip = "127.0.0.1"
        port = "41415"
        ipAdrr = "%s:%s" % (ip, port)

        forward_cmd = "adb forward tcp:%s tcp:%s" % (port, port)
        rm_img_cmd = "adb shell rm -rf /sdcard/tempimg/"

        forward = os.popen(forward_cmd)
        forward = os.popen(rm_img_cmd)

    Fuzz(ipAdrr).get_packages(temp_root_path)
