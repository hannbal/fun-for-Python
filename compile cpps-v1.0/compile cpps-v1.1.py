# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Tony\python\window\1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.Qsci import  QsciLexerCPP
from PyQt5 import *
import win32api, re, shutil, os.path, sys, win32gui, win32con
from winreg import *
#import highlinghter

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
        
#use TextEdit and PythonHighlighter do Highlight job         
#       self.QPlainTextEdit_1 = QtWidgets.QTextBrowser(Dialog）
#        self.QPlainTextEdit_1.setGeometry(QtCore.QRect(250, 30, 931, 461))
#        self.QPlainTextEdit_1.setObjectName("QPlainTextEdit_1")
#        self.QPlainTextEdit_1.setReadOnly(0)
#        self.QPlainTextEdit_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
#        self.QPlainTextEdit_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.QPlainTextEdit_1 =  Qsci.QsciScintilla(Dialog)
        self.QPlainTextEdit_1.setGeometry(QtCore.QRect(250, 30, 931, 461))
        self.QPlainTextEdit_1.setObjectName("QPlainTextEdit_1")
        self.QPlainTextEdit_1.setMarginType(1, Qsci.QsciScintilla.NumberMargin)
        self.QPlainTextEdit_1.setMarginWidth(1, 20)
        self.QPlainTextEdit_1.setMarginLineNumbers(1, True)
        self.QPlainTextEdit_1.SendScintilla(Qsci.QsciScintilla.SCI_SETCODEPAGE, Qsci.QsciScintilla.SC_CP_UTF8)       
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(250, 500, 931, 231))
        self.textBrowser_2.setObjectName("textBrowser_2")

#        self.verticalScrollBar = QtWidgets.QScrollBar(Dialog)
#        self.verticalScrollBar.setGeometry(QtCore.QRect(1150, 40, 20, 411))
#        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
#        self.verticalScrollBar.setObjectName("verticalScrollBar")
#        self.horizontalScrollBar = QtWidgets.QScrollBar(Dialog)
#        self.horizontalScrollBar.setGeometry(QtCore.QRect(330, 470, 731, 16))
#        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
#        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
#        self.verticalScrollBar_2 = QtWidgets.QScrollBar(Dialog)
#        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1160, 510, 20, 211))
#        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
#        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
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
            QMessageBox.information(self.pushButton_3, "Warring", "Please choose the folder！", QMessageBox.Ok)
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
                QMessageBox.information(self.pushButton_3, "Warring", "\'exe\'file did not export！", QMessageBox.Ok)
                
        
        
    def buttonclicked_BrowFile(self, event):
        dirname = QFileDialog.getExistingDirectory(self.pushButton_1,"Please choose folder ", self.FilePath)
        self.list_dir.clear()
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
                pattern=re.compile(r'id_\d{5,7}_[\u4e00-\u9fa5)+]{2,5}_\d{1,2}_\d{1,2}.cpp')
                if (file_name!=''):
                    pattern = re.compile(r'_\d{5,7}_')
                    st_number=pattern.findall(file_name)[0]
                    pattern=re.compile(r'_\d{1,2}_\d{1,2}')
                    cpp_number = pattern.findall(file_name)[0]
                    pattern=re.compile(u"[\u4e00-\u9fa5]+")
                    st_name= pattern.findall(file_name)[0]
                    new_filename='id'+st_number+st_name+cpp_number+'.cpp'
                    os.rename( self.FilePath+'\\'+file_name,  self.FilePath+'\\'+new_filename)
                    file_name = new_filename
                self.list_dir.addItem(str(file_name))    
    
    
    def buttonclicked_ModifyFile(self, event):
        filepath = self.FilePath+'/'
        if (self.list_dir.currentItem()):
            filepath += str(self.list_dir.currentItem().text())
            print(filepath)
            if os.path.isfile(filepath):
#                win32api.ShellExecute(0, 'open','notepad.exe', filepath,'',  1)
                with open(filepath, 'w')as tmp:
                    print(self.QPlainTextEdit_1.text())
                    tmp.write(self.QPlainTextEdit_1.text())
            else:
                QMessageBox.information(self.pushButton_2, "Warring", "The folder does not exist！", QMessageBox.Ok)
        else:
            QMessageBox.information(self.pushButton_2, "warring", "Please choose the folder！", QMessageBox.Ok)
        
    def buttonclicked_ReadFile(self, event):
        filepath = self.lineEdit.text()+'//'+str(self.list_dir.currentItem().text())
        with open(filepath, "r")as tmp1:
            self.QPlainTextEdit_1.setText(tmp1.read())
            tmp1.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "C++批改-v1.0"))
        self.lineEdit.setText(_translate("Dialog", self.FilePath))
        self.pushButton_1.setText(_translate("Dialog", "浏览"))
        self.pushButton_2.setText(_translate("Dialog", "保存"))
        self.pushButton_3.setText(_translate("Dialog", "Run"))
        self.pushButton_4.setText(_translate("Dialog", "刷新"))

def setenv(env_path, env_lib, env_inculde):
    str_ide=''
    str_bin=''
    str_include=''
    str_lib=''
    reg_dirname = re.compile(r'Microsoft Visual Studio \d{1,2}.\d')  
    for parent, dirnames, filenames in os.walk(rootdir):
         for dirname in dirnames:
            if (reg_dirname.match(dirname)):
                strfilepath = parent+os.sep+dirname
                if(os.path.exists(strfilepath+'\\VC\\bin')):
                    str_bin = strfilepath+'\\VC\\bin'
#                      print('binfound!')
                    if(os.path.exists(strfilepath+'\\Common7\\IDE')):
#                        print('idefound!')
                        str_ide=strfilepath+'\\Common7\\IDE;'
                    if(os.path.exists(strfilepath+'\\VC\\include')):
#                        print('includefound!')
                        str_include=strfilepath+'\\VC\\include'
                    if(os.path.exists(strfilepath+'\\VC\\lib')):
#                        print('libfound!')
                        str_lib=strfilepath+'\\VC\\lib'

    str_err=''
    t_path=''
    t_include=''
    t_lib=''
    if(str_ide):
        if(env_path==None or env_path.find(str_ide)==-1):
            t_path = ';'+str_ide
    else:
        str_err +='IDE,'
    
    if(str_bin):
        if(env_path ==None or env_path.find(str_bin)==-1):
            t_path +=';'+str_bin
    else:
        str_err +='BIN,'
    
    if(str_include):
        if(env_include ==None or env_include.find(str_include)==-1):
            t_include +=';'+str_include
    else:
        str_err+='INCLUDE,'
#        print(str_include)
#        print(env_include)
    
    if(str_lib):
        if(env_lib ==None or env_lib.find(str_lib)==-1):
            t_lib =str_lib
    else:
        str_err+='LIB,'
    
    if(str_err):
        win32api.MessageBox(0, "Folder"+str_err+"is not in VC folder！Please make sure Visual Studio is instlled!", "Warring Message", win32con.MB_OK)
    else:
        if(t_path):
            if(env_path):
                osstr="setx /m PATH \"%PATH%;"+t_path+"\""
            else:
                osstr="setx /m PATH \""+t_path+"\""
            print(osstr)
            os.popen(osstr)
        if(t_include):
            if(env_include):
                osstr="setx /m INCLUDE \"%INCLUDE%;"+t_include+"\""
            else:
                osstr="setx /m INCLUDE \""+t_include+"\""
            print(osstr)
            os.popen(osstr) 
        if(t_lib):
            if(env_lib):
                osstr="setx /m LIB \"%LIB%;"+t_lib+"\""
            else:
                osstr="setx /m LIB \""+t_lib+"\""
            print(osstr)
            os.popen(osstr) 
        return(str_lib)
    
if __name__ == "__main__":
    import sys
    env_path= os.getenv('PATH')
    env_lib=os.getenv('LIB')
    env_include=os.getenv('INCLUDE')
    
    rs_ide=''
    rs_bin=''
    rs_include=''
    rs_lib=''
    rootdir ='c:\\'
#    reg_dirname = re.compile(r'c:\\[^;]*Microsoft Visual Studio \d{1,2}.\d(((\\VC\\lib|\\Common7\\IDE)|\\VC\\bin)|\\VC\\include)',re.I)
#    it = reg_dirname.finditer(a)
#    for match in it:
#        print(match.group())
    reg_bin = re.compile(r'c:\\[^;]*Microsoft Visual Studio \d{1,2}.\d\\VC\\bin',re.I)
    if(env_path and reg_bin.search(env_path)):
        rs_bin = reg_bin.search(env_path).group()
    reg_ide = re.compile(r'c:\\[^;]*Microsoft Visual Studio \d{1,2}.\d\\Common7\\IDE',re.I)
    if(env_path and reg_ide.search(env_path)):
        rs_ide = reg_ide.search(env_path).group()
    reg_lib = re.compile(r'c:\\[^;]*Microsoft Visual Studio \d{1,2}.\d\\VC\\lib',re.I)
    if(env_lib and reg_lib.search(env_lib)):
        rs_lib=reg_lib.search(env_lib).group()
    reg_include = re.compile(r'c:\\[^;]*Microsoft Visual Studio \d{1,2}.\d\\VC\\include',re.I)
    if(env_include and reg_include.search(env_include)):
        rs_include=reg_include.search(env_include).group()
    
    if(rs_bin and os.path.exists(rs_bin)):
        if (rs_ide and os.path.exists(rs_ide)):
            if(rs_lib and os.path.exists(rs_lib)):
                if(rs_include and os.path.exists(rs_include)):
                    print('your computer do not need set environment')
                    strfilepath=rs_lib
                else:
                    strfilepath=setenv(env_path, env_lib, env_include)
#                    env_lib=os.getenv('LIB')
#                    strfilepath= reg_lib.search(env_lib).group()
            else:
                strfilepath=setenv(env_path, env_lib, env_include)
#                env_lib=os.getenv('LIB')
#                print(env_lib)
#                strfilepath= reg_lib.search(env_lib).group()
        else:
            strfilepath=setenv(env_path, env_lib, env_include)
#            env_lib=os.getenv('LIB')
#            strfilepath= reg_lib.search(env_lib).group()
    else:
        strfilepath=setenv(env_path, env_lib, env_include)
#        env_lib=os.getenv('LIB')
#        print(env_lib)
#        strfilepath= reg_lib.search(env_lib).group()
        
    if(os.path.isfile(strfilepath+'\\Kernel32.Lib')==False):
        print(strfilepath+'\\Kernel32.Lib')
        cpath=os.getcwd()+'\\Kernel32.Lib'
        if(os.path.isfile(cpath)):
            tpath=strfilepath+'\\Kernel32.Lib'
            shutil.copyfile(cpath, tpath)
        else:
            win32api.MessageBox(0, "\'Kernel32.Lib\' file is not in the currect folder,please copy it to folder \'VC\\lib\'!", "Warring Message", win32con.MB_OK)
            sys.exit()
    
    if(rs_ide!='' and rs_bin!= '' and rs_include !='' and rs_lib!=''):
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.QPlainTextEdit_1.setLexer(QsciLexerCPP())
#        hightlight=highlinghter.PythonHighlighter(ui.QPlainTextEdit_1.document())
        Dialog.show()
        sys.exit(app.exec_())
    else:
        win32api.MessageBox(0, "We have set environment for you,please restart the cpps.exe", "Warring Message", win32con.MB_OK)
        sys.exit()

