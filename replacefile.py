# -*- coding: UTF-8 -*-
import os
import shutil
import xlrd
import time
import sys
import subprocess

bat_path = "\\exe_file\\exe\\"

class Execl(object):

    def __init__(self,config_path):
        self.config_path =config_path

    def readexcel(self):
        wb = xlrd.open_workbook(filename=self.config_path)  # 打开文件
        sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
        rownum = sheet1.nrows
        datalist = []
        for i in range(rownum):
            datalist.append(sheet1.row_values(i))
        return datalist

def run_server(path):
    os.chdir(path)
    p1 = subprocess.Popen(path + "start_global.bat",shell=True)
    time.sleep(2)
    p2 = subprocess.Popen(path+"start_allserver.bat",shell=True)
    # os.system("start " + path + "start_global.bat")
    # time.sleep(2)
    # os.system("start "+path+"start_allserver.bat")
    time.sleep(2)

def run_script(project_dir,config_file_path):
    exe_file = ""
    if not os.path.exists(project_dir):
        return (False, None)
    if os.path.exists(project_dir+"\\exe_file"):
        exe_file = "\\exe_file"
        print(222)
    filepath = sys.argv[0]
    realpath = os.path.realpath(filepath)
    current_path = os.path.dirname(realpath)
    config_path = current_path+"\\dgm_config\\config.xlsx"
    replace_path = current_path + config_file_path
    read_config = Execl(config_path)
    config_list = read_config.readexcel()
    replace_file_list = os.listdir(replace_path)

    try:
        for file in replace_file_list:
            for config_file in config_list:
                if file in config_file:
                    src = replace_path+file
                    dst = project_dir+exe_file+config_file[1]+file
                    print(src)
                    print(dst)
                    shutil.copyfile(src,dst)
                    print('执行成功')
        return (True,project_dir)
    except Exception as e:
        print('项目路径不正确')
        return (False,None)




