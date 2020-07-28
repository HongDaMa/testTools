# -*- coding: utf-8 -*-
#pragma execution_character_set("utf-8")
# Form implementation generated from reading ui file 'autotools.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog,QWidget,QInputDialog,QLineEdit
import massage
import os
import replacefile
import json
import shutil
import sys

class Ui_MainWindow(QWidget):

    def __init__(self, name = 'MainForm',):
        super().__init__()
        self.cwd = os.getcwd() # 获取当前程序文件位置
        self.dir_list = []
        self.server_list = []
        self.bat_path = "\\exe\\"
        self.complete_replace = False #是否替换完成
        self.version_dir = None
        self.dir_choose = None

    #读配置文件
    def read_config_file(self):
        #重置当前目录
        filepath = sys.argv[0]
        realpath = os.path.realpath(filepath)
        current_path = os.path.dirname(realpath)
        os.chdir(current_path)

        f = open("config_info.json", encoding='utf-8')
        setting = json.load(f)
        f.close()
        return setting
    #问配置文件
    def write_config_file(self,json_config):
        jsondata = json.dumps(json_config, ensure_ascii=False)
        f = open('config_info.json', 'w', encoding="utf-8")
        f.write(jsondata)
        f.close()

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 451, 221))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.VLayout_1 = QtWidgets.QVBoxLayout(self.tab)
        self.VLayout_1.setObjectName("VLayout_1")

        # 第一排
        self.HLayout_1 = QtWidgets.QHBoxLayout()
        self.HLayout_1.setObjectName("HLayout_1")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.HLayout_1.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.HLayout_1.addWidget(self.lineEdit)
        self.btn_chooseDir = QtWidgets.QPushButton(self.tab)
        self.btn_chooseDir.setObjectName("btn_chooseDir")
        self.HLayout_1.addWidget(self.btn_chooseDir)
        self.VLayout_1.addLayout(self.HLayout_1)

        #第二排
        self.HLayout_2 = QtWidgets.QHBoxLayout()
        self.HLayout_2.setObjectName("HLayout_2")
        self.HLayout_2.addStretch(2)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color:blue")
        self.VLayout_1.addLayout(self.HLayout_2)
        self.HLayout_2.addWidget(self.label_3)

        #第三排
        self.HLayout_3 = QtWidgets.QHBoxLayout()
        self.HLayout_3.setObjectName("HLayout_3")
        self.checkbox_version = QtWidgets.QCheckBox(self.tab)
        self.checkbox_version.setObjectName("checkbox_version")
        self.HLayout_3.addWidget(self.checkbox_version)
        self.edit_version = QtWidgets.QLineEdit(self.tab)
        self.edit_version.setObjectName("edit_version")
        self.HLayout_3.addWidget(self.edit_version)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.HLayout_3.addWidget(self.label_2)
        self.VLayout_1.addLayout(self.HLayout_3)

        self.cut_off_rule = QtWidgets.QLabel()
        self.cut_off_rule.setText("选择要替换的配置↓：")
        self.VLayout_1.addWidget(self.cut_off_rule)

        # 第四排
        self.combobox_config = QtWidgets.QComboBox()
        self.combobox_config.setObjectName("combobox_config")
        self.btn_delete_config = QtWidgets.QPushButton()
        self.btn_delete_config.setObjectName("btn_delete_config")
        self.HLayout_4 = QtWidgets.QHBoxLayout()
        self.HLayout_4.setObjectName("HLayout_4")
        self.HLayout_4.addWidget(self.combobox_config)
        self.HLayout_4.addWidget(self.btn_delete_config)
        self.HLayout_4.setStretchFactor(self.combobox_config,2.5)
        self.HLayout_4.setStretchFactor(self.btn_delete_config, 1)
        self.VLayout_1.addLayout(self.HLayout_4)

        # 第五排
        self.HLayout_6 = QtWidgets.QHBoxLayout()
        self.HLayout_6.setObjectName("HLayout_6")
        self.btn_determine = QtWidgets.QPushButton(self.tab)
        self.btn_determine.setObjectName("btn_determine")
        self.HLayout_6.addWidget(self.btn_determine)
        self.btn_save = QtWidgets.QPushButton(self.tab)
        self.btn_save.setObjectName("btn_save")
        self.HLayout_6.addWidget(self.btn_save)
        self.VLayout_1.addLayout(self.HLayout_6)

        #第六排
        self.HLayout_5 = QtWidgets.QHBoxLayout()
        self.HLayout_5.setObjectName("HLayout_5")
        self.btn_runsever = QtWidgets.QPushButton(self.tab)
        self.btn_runsever.setObjectName("btn_runsever")
        self.HLayout_5.addWidget(self.btn_runsever)
        self.btn_GMtools = QtWidgets.QPushButton()
        self.btn_GMtools.setObjectName("btn_GMtools")
        self.HLayout_5.addWidget(self.btn_GMtools)
        self.btn_openroot = QtWidgets.QPushButton()
        self.btn_openroot.setObjectName("btn_openroot")
        self.HLayout_5.addWidget(self.btn_openroot)
        self.VLayout_1.addLayout(self.HLayout_5)



        #添加标签页
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "私服配置替换工具"))
        MainWindow.setWindowIcon(QIcon('tools.jpg'))
        self.label.setText(_translate("MainWindow", "炫舞手游项目路径："))
        self.btn_chooseDir.setText(_translate("MainWindow", "选择路径"))
        self.btn_GMtools.setText(_translate("MainWindow","启动GM工具"))
        self.btn_delete_config.setText("删除配置")
        self.btn_GMtools.setStyleSheet("color:green")
        self.btn_openroot.setText("打开项目根目录")
        self.btn_openroot.setStyleSheet("color:purple")
        self.btn_runsever.setText(_translate("MainWindow", "运行私服服务器"))
        self.btn_runsever.setStyleSheet("color:red")
        self.label_3.setText("当前P4号：无")
        self.checkbox_version.setText(_translate("MainWindow", "替换指定版本号"))
        self.label_2.setText(_translate("MainWindow", "注意：不勾选则替换最高版本私服"))
        self.btn_determine.setText(_translate("MainWindow", "替换"))
        self.btn_save.setText(_translate("MainWindow", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "DGM私服配置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "炫舞时代项目"))

        self.combobox_config.addItem("    ======   请 选 择 配 置 方 案   ======   ")

        #绑定信号
        self.bind_event()

    def bind_event(self):
        self.btn_runsever.clicked.connect(self.slot_btn_runsever)
        self.btn_chooseDir.clicked.connect(self.slot_btn_chooseDir)
        self.btn_determine.clicked.connect(self.slot_btn_determine)
        self.btn_save.clicked.connect(self.slot_btn_save)
        self.lineEdit.textEdited[str].connect(lambda: self.slot_lineedit_onChange())
        self.btn_openroot.clicked.connect(self.slot_btn_openroot)
        self.btn_GMtools.clicked.connect(self.slot_btn_GMtools)
        self.btn_delete_config.clicked.connect(self.slot_btn_delete_config)

    def slot_lineedit_onChange(self):
        self.dir_choose = self.lineEdit.text()

    def slot_btn_delete_config(self):
        if self.combobox_config.currentIndex() != 0:
            config_info = self.read_config_file()

            filepath = sys.argv[0]
            realpath = os.path.realpath(filepath)
            current_path = os.path.dirname(realpath)
            config_path = current_path + "\\dgm_config\\"+self.combobox_config.currentText()+"\\"
            shutil.rmtree(config_path,True)
            config_info["item"].pop(self.combobox_config.currentIndex() - 1)
            config_info['current_index'] = config_info['current_index'] - 1
            self.write_config_file(config_info)
            self.combobox_config.removeItem(self.combobox_config.currentIndex())
        else:
            pass

    def slot_btn_save(self):
        if self.complete_replace:
            config_name, ok = QInputDialog.getText(self, "保存配置", "请输入修改新增配置的名称:", QLineEdit.Normal, "配置方案1")
            self.save_config_scheme(config_name)
        else:
            massage.error_no_replace()

    def slot_btn_runsever(self):
        exe_file = self.find_exe_file()
        setting = self.read_config_file()
        if setting:
            setting = self.read_config_file()
            replacefile.run_server(setting['last']['path']+setting['last']['version_number']+exe_file+self.bat_path)
        else:
            massage.error_no_replace()

    def slot_btn_openroot(self):
        setting = self.read_config_file()
        if setting:
            os.system("start explorer "+setting['last']['path']+setting['last']['version_number'])
        else:
            massage.error_no_replace()

    def slot_btn_GMtools(self):
        exe_file = self.find_exe_file()
        setting = self.read_config_file()
        if setting:
            path = setting['last']['path']+setting['last']['version_number']+exe_file+"\\exe\\bin\\"
            os.chdir(path)
            os.system("start "+path+"GMClient.exe")
        else:
            massage.error_no_replace()

    def slot_btn_determine(self):
        #检查项目路径是否为空
        if not self.lineEdit.text():
            return massage.error_no_choose_path()
        if self.checkbox_version.isChecked() and not self.edit_version.text():
            return massage.error_no_version_number()
        tag = False
        result = False
        success_path = ""
        config_file_path = "\\dgm_config\\server\\"
        current_config_id = self.combobox_config.currentIndex()

        if self.combobox_config.currentIndex() != 0 :
            # 替换已保存的配置
            config_file_path = "\\dgm_config\\" + self.read_config_file()["item"][self.combobox_config.currentIndex() - 1] + "\\"

            if self.checkbox_version.isChecked():
                self.version_dir = self.edit_version.text()
            else:
                self.version_dir, tag = self.order_by_version(self.dir_choose)
                if tag == False:
                    return massage.error_path()

            result, success_path = replacefile.run_script(self.dir_choose + self.version_dir, config_file_path)

        else:
            # 替换新的配置
            if self.checkbox_version.isChecked():
                self.version_dir = self.edit_version.text()
                result, success_path = replacefile.run_script(self.dir_choose + self.version_dir,config_file_path)
            else:
                # 运行替换脚本
                self.version_dir,tag = self.order_by_version(self.dir_choose)
                if tag == True:
                    result,success_path = replacefile.run_script(self.dir_choose + self.version_dir,config_file_path)
                else:
                    result = False

        if result:

            config_info = self.read_config_file()
            config_info['current_index'] = self.combobox_config.currentIndex()-1
            last_repale_info ={"last": {'path': self.dir_choose, 'version_number': self.version_dir}}
            config_info.update(last_repale_info)
            self.write_config_file(config_info)

            self.label_3.setText("当前P4号:" + self.version_dir)
            self.complete_replace = True
            return massage.success(success_path)
        else:
            return massage.error_path()

    def slot_btn_chooseDir(self):
        edit_inpunt_dir = QFileDialog.getExistingDirectory(self,"选取文件夹",self.cwd) # 起始路径
        edit_inpunt_dir = edit_inpunt_dir.replace("/","\\")+"\\"
        self.lineEdit.setText(edit_inpunt_dir)
        self.dir_choose = self.lineEdit.text()

    #将替换好的文件生成新的配置文件夹
    def save_config_scheme(self,name):
        filepath = sys.argv[0]
        realpath = os.path.realpath(filepath)
        current_path = os.path.dirname(realpath)
        new_config_dir = current_path + "\\dgm_config\\" + name +"\\"
        os.chdir(current_path)
        if os.path.exists(new_config_dir):
            massage.error_dir_exits()
            return
        else:
            os.mkdir(new_config_dir)
        replace_path = current_path + "\\dgm_config\\server\\"
        replace_file_list = os.listdir(replace_path)

        try:
            for file in replace_file_list:
                src = replace_path + file
                dst = new_config_dir + file
                shutil.move(src, dst)
        except Exception as e:
            massage.error_no_save()

        #保存配置文件
        self.combobox_config.addItem(name)
        self.combobox_config.setCurrentIndex(self.combobox_config.count()-1)
        # json_config = {name:{'path': self.dir_choose, 'version_number': self.version_dir}}
        # json_config = {}
        config_info = self.read_config_file()
        if config_info.get("item"):
            config_info['item'].append(name)
        else:
            config_info["item"] = []
            config_info['item'].append(name)
        config_info['current_index'] = self.combobox_config.count() - 2
        # config_info.update(json_config)
        self.write_config_file(config_info)

        massage.save_success()

    def order_by_version(self,path):
        #递归一层
        # print(path)
        if path == '\\' or path == '/':
            return ([], False)
        for root, dirs, files in os.walk(path):
            self.dir_list = dirs
            break
        self.server_list = []
        if self.dir_list:
            for item in self.dir_list:
                if item.isdecimal():
                    self.server_list.append(item)
            self.server_list=list(map(int,self.server_list))
            self.server_list.sort(reverse=True)
            self.server_list = list(map(str, self.server_list))
            if self.server_list:
                return (self.server_list[0],True)
        return ([],False)

    def find_exe_file(self):
        setting = self.read_config_file()
        if os.path.exists(setting['last']['path'] + setting['last']['version_number']+"\\exe_file"):
            return "\\exe_file"
        else:
            return ""

