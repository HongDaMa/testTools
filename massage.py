# -- coding: utf-8 --
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

# class Message(object):
#     def __init__(self):
#         self.title_waining = "警告"
#         self.title_hint = "提示"
#
#     def template(self,title,text):
#         reply = QMessageBox()
#         reply.setWindowTitle(title)
#         reply.setText(text)
#         reply.addButton(QtWidgets.QPushButton('好的'), QMessageBox.YesRole)
#         reply.exec()
#
#     def error_no_replace(self):
#         self.template(self.title_waining,"请先替换配置在运行此功能")
#
#     def error_no_choose_path(self):
#         self.template(self.title_waining,'请选择项目路径')
#
#     def error_no_version_number(self):
#         self.template(self.title_waining,'请输入版本号在执行操作')
#
#     def error_path(self):
#         self.template(self.title_waining,"项目路径不正确或者发生未知错误")
#
#     def error_no_save(self):
#         self.template(self.title_waining,'发生致命错误！无法保存配置方案')
#
#     def error_dir_exits(self):
#         self.template(self.title_waining,'当前配置名称已存在！请更换其他配置名称')
#
#     def success(success_path):
#         reply = QMessageBox()
#         reply.setWindowTitle('提示')
#         reply.setText('目标路径:' + success_path + '执行成功')
#         reply.addButton(QtWidgets.QPushButton('好的'), QMessageBox.YesRole)
#         reply.exec()
#
#     def save_success(self):
#         self.template(self.title_hint,'配置保存成功')

def error_no_replace():
    reply = QMessageBox()
    reply.setWindowTitle('警告')
    reply.setText('请先替换配置在运行此功能')
    reply.addButton(QtWidgets.QPushButton('好的'), QMessageBox.YesRole)
    reply.exec()

def error_no_choose_path():
    reply = QMessageBox()
    reply.setWindowTitle('警告')
    reply.setText('请选择项目路径')
    reply.addButton(QtWidgets.QPushButton('好的'), QMessageBox.YesRole)
    reply.exec()

def error_no_version_number():
    reply = QMessageBox()
    reply.setWindowTitle('警告')
    reply.setText('请输入版本号在执行操作')
    reply.addButton(QtWidgets.QPushButton('确认'), QMessageBox.YesRole)
    reply.exec()

def error_path():
    reply = QMessageBox()
    reply.setWindowTitle('警告')
    reply.setText('项目路径不正确或者发生未知错误')
    reply.addButton(QtWidgets.QPushButton('确认'), QMessageBox.YesRole)
    reply.exec()

def success(success_path):
    reply = QMessageBox()
    reply.setWindowTitle('提示')
    reply.setText('目标路径:' + success_path + '执行成功')
    reply.addButton(QtWidgets.QPushButton('好的'), QMessageBox.YesRole)
    reply.exec()

def error_no_save():
    reply = QMessageBox()
    reply.setWindowTitle('警告')
    reply.setText('发生致命错误！无法保存配置方案')
    reply.addButton(QtWidgets.QPushButton('确认'), QMessageBox.YesRole)
    reply.exec()

def error_dir_exits():
    reply = QMessageBox()
    reply.setWindowTitle('警告')
    reply.setText('当前配置名称已存在！请更换其他配置名称')
    reply.addButton(QtWidgets.QPushButton('确认'), QMessageBox.YesRole)
    reply.exec()

def save_success():
    reply = QMessageBox()
    reply.setWindowTitle('提示')
    reply.setText('配置保存成功')
    reply.addButton(QtWidgets.QPushButton('好的'), QMessageBox.YesRole)
    reply.exec()
