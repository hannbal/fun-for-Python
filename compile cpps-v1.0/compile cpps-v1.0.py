# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Tony\python\window\1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import win32api

class Ui_Dialog(object):
    FilePath=os.getcwd()
    currectPath = os.getcwd()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        Dialog.setMinimumSize(QtCore.QSize(1200, 800))
        Dialog.setSizeGripEnabled(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(870, 740, 341, 40))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.list_dir = QtWidgets.QListWidget(Dialog)
        self.list_dir.setGeometry(QtCore.QRect(10, 90, 231, 641))
        self.list_dir.setObjectName("listView")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(250, 30, 931, 461))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(250, 500, 931, 231))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1150, 40, 20, 411))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalScrollBar = QtWidgets.QScrollBar(Dialog)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(330, 470, 731, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1160, 510, 20, 211))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 60, 61, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 748, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 748, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 748, 61, 23))
        self.pushButton_4.setObjectName("pushButton_3")
        
        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton_1.clicked.connect(self.buttonclicked_BrowFile)
        self.pushButton_2.clicked.connect(self.buttonclicked_ModifyFile)
        self.pushButton_3.clicked.connect(self.buttonclicked_Run)
        self.pushButton_4.clicked.connect(self.buttonclicked_ReadFile)
        self.list_dir.clicked.connect(self.buttonclicked_ReadFile)
    
    def buttonclicked_Run(self, event):
        if self.list_dir.count()==0:
#            reply = QMessageBox.information(self.pushButton_3, "提示", "请选择CPP文件！", QMessageBox.Ok)
#            self.pushButton_3.echo(reply)
            QMessageBox.information(self.pushButton_3, "提示", "请导入文件夹并选择CPP文件！", QMessageBox.Ok)
        else:
            filename = str(self.list_dir.currentItem().text())
            cppfile =  self.FilePath+'//'+filename
            osstr="cd "+ self.FilePath+"&&cl /EHsc "+cppfile
            self.textBrowser_2.setText(os.popen(osstr).read())
#            print(self.currectPath+'//'+filename[:-4]+'.exe')
            exefile = cppfile[:-4]+".exe" 
            if os.path.isfile(exefile):
                win32api.ShellExecute(0, 'open', exefile, '','',1)
            elif os.path.isfile(self.currectPath+'//'+filename[:-4]+'.exe'):
                win32api.ShellExecute(0, 'open', self.currectPath+'//'+filename[:-4]+'.exe', '','',1)
            else:
                QMessageBox.information(self.pushButton_3, "提示", "exe文件未生成或不在默认目录中！", QMessageBox.Ok)
                
        
        
    def buttonclicked_BrowFile(self, event):
        dirname = QFileDialog.getExistingDirectory(self.pushButton_1,"选择文件夹", self.FilePath)
        if dirname !='':
            self.lineEdit.setText(dirname)
            self.FilePath = dirname
            file_stdafx = "stdafx.h"
            if (os.path.isfile(dirname+'//'+file_stdafx)==False):
                with open(dirname+'//'+file_stdafx, 'w')as tmp1:
                    tmp1.close
                
                
        else:
            dirname = self.FilePath
        allfiles = os.listdir(self.lineEdit.text())
        for file_name in allfiles:
            if (file_name[-4:] == ".cpp"):
                self.list_dir.addItem(str(file_name))    
    
    
    def buttonclicked_ModifyFile(self, event):
        filepath = self.FilePath+'/'
        if (self.list_dir.currentItem()):
            filepath += str(self.list_dir.currentItem().text())
            print(filepath)
            if os.path.isfile(filepath):
                win32api.ShellExecute(0, 'open','notepad.exe', filepath,'',  1)
            else:
                QMessageBox.information(self.pushButton_2, "提示", "选择的文件不存在！", QMessageBox.Ok)
        else:
            QMessageBox.information(self.pushButton_2, "提示", "请导入文件夹并选择CPP文件！", QMessageBox.Ok)
        
    def buttonclicked_ReadFile(self, event):
        filepath = self.lineEdit.text()+'//'+str(self.list_dir.currentItem().text())
        with open(filepath, "r")as tmp1:
            self.textBrowser.setText(tmp1.read())
            tmp1.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "C++批改-v1.0"))
        self.lineEdit.setText(_translate("Dialog", self.FilePath))
        self.pushButton_1.setText(_translate("Dialog", "浏览"))
        self.pushButton_2.setText(_translate("Dialog", "修改"))
        self.pushButton_3.setText(_translate("Dialog", "Run"))
        self.pushButton_4.setText(_translate("Dialog", "刷新"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

