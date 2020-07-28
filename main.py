# -*- coding: UTF-8 -*-
#pragma execution_character_set("utf-8")
import sys
import autotools2
from PyQt5.QtWidgets import QApplication, QMainWindow
import json

def init():
    f = open("config_info.json", encoding='utf-8')
    setting = json.load(f)
    ui = autotools2.Ui_MainWindow()
    if setting.get('last'):
        ui.setupUi(MainWindow)
        ui.lineEdit.setText(setting["last"]['path'])
        ui.dir_choose = setting["last"]['path']
        ui.label_3.setText("当前P4号:" + setting["last"]['version_number'])
        if setting.get('item'):
            for item in setting['item']:
                ui.combobox_config.addItem(item)
        ui.combobox_config.setCurrentIndex(setting['current_index'] + 1)
    else:
        ui.setupUi(MainWindow)
        ui.dir_choose = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    init()
    MainWindow.show()
    sys.exit(app.exec())