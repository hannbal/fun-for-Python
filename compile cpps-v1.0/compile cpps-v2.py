# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Tony\python\window\1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qsci import  QsciLexerCPP
from PyQt5 import *
import win32api, re, shutil, os.path, sys, win32con
from winreg import *
from PyQt5.QtGui import QColor
#import highlinghter
#import highlinghter

class Ui_Dialog(object):
    env_path= os.getenv('PATH')
    env_lib=os.getenv('LIB')
    env_include=os.getenv('INCLUDE')
    allfiles={}
    col = QColor(0, 0, 0)
    cppdircount=0
    
    FilePath=os.getcwd()
    currectPath = os.getcwd()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "C++批改-v2"))
        self.lineEdit.setText(_translate("Dialog", self.FilePath))
        self.pushButton_1.setText(_translate("Dialog", "浏览"))
        self.pushButton_2.setText(_translate("Dialog", "保存"))
        self.pushButton_3.setText(_translate("Dialog", "Run"))
        self.pushButton_4.setText(_translate("Dialog", "刷新"))
        self.pushButton_5.setText(_translate("Dialog", "设置"))
        self.radioButton.setText(_translate("Dialog", "自动设置VS目录（时间较长）"))
        self.radioButton_2.setText(_translate("Dialog", "手动设置VS目录"))
        self.lineEdit_2.setText(_translate("Dialog", "c:\\"))              
        
    
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
        self.textBrowser_2.setStyleSheet("QTextBrowser{background-color: black;font: 16px;color: white;}")
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
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 750, 98, 26))
        self.pushButton_5.setObjectName("pushButton_3")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(20, 740, 271, 22))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 770, 251, 22))
        self.radioButton_2.setObjectName("radioButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 770, 231, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")  
        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)        
        self.pushButton_1.clicked.connect(self.buttonclicked_BrowFile)
        self.pushButton_2.clicked.connect(self.buttonclicked_ModifyFile)
        self.pushButton_3.clicked.connect(self.buttonclicked_Run)
        self.pushButton_4.clicked.connect(self.buttonclicked_ReadFile)
        self.list_dir.clicked.connect(self.buttonclicked_ReadFile)
        self.pushButton_5.clicked.connect(self.setenv)
        
    
    def buttonclicked_Run(self, event):
        if self.list_dir.currentItem() ==None:
            QMessageBox.information(self.pushButton_3, "Warring", "Please choose the folder and cpp file！", QMessageBox.Ok)
        else:
            filename = str(self.list_dir.currentItem().text())
            cppfile =  self.allfiles[filename]+filename
            osstr="cd "+'"'+ str(self.allfiles[filename])+'"'+" && cl /EHsc "+'"'+str(cppfile.replace("//", "\\"))+'"'
            extext=os.popen(osstr).read()
            self.textBrowser_2.setText(extext)
            exefile = filename[:-4]+".exe" 
            if os.path.isfile(exefile):
                win32api.ShellExecute(0, 'open', exefile, '','',1)
            elif os.path.isfile(cppfile[:-4]+'.exe'):
                win32api.ShellExecute(0, 'open', cppfile[:-4]+'.exe', '','',1)
            else:
                QMessageBox.information(self.pushButton_3, "Warring", "\'exe\'file did not export！", QMessageBox.Ok)
                
    def scandirs(self, path):
        files_list={}
        
        for parent, dirnames, filenames in os.walk(path):
            for dirname in dirnames:
                self.scandirs(parent+dirname)
            for filename in filenames:
                if filename[-4:]==".cpp":
                    files_list.update({filename:parent.replace("/", "\\")+"\\"})
                    self.list_dir.addItem(str(filename))  
        return files_list
    
    
    def buttonclicked_BrowFile(self, event):
        dirname = QFileDialog.getExistingDirectory(self.pushButton_1,"Please choose folder ", self.FilePath)
        self.list_dir.clear()
        if dirname !='':
            self.lineEdit.setText(dirname)
            self.FilePath = dirname
            file_stdafx = "stdafx.h"
            if (os.path.isfile(dirname+'//'+file_stdafx)==False):
                try:
                    with open(dirname+'//'+file_stdafx, 'w')as tmp1:
                        tmp1.close
                except Exception :
                    QMessageBox.information(self.pushButton_1, "Error", "Please choose right folder", QMessageBox.Ok)
        else:
            dirname = self.FilePath
            
        self.allfiles= self.scandirs(dirname)
        if len(self.allfiles)==0:
            win32api.MessageBox(0, "There is none cpp files in "+dirname, "Warring Message", win32con.MB_OK)
     

    def buttonclicked_ModifyFile(self, event):
        filename=self.list_dir.currentItem().text()
        filepath = self.allfiles[filename]
        if (filename):
            filepath += filename
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
#        print(self.allfiles)
        filepath = self.allfiles[str(self.list_dir.currentItem().text())]+str(self.list_dir.currentItem().text())
        try:
            with open(filepath, "r")as tmp1:
                self.QPlainTextEdit_1.setText(tmp1.read())
            tmp1.close()
        except UnicodeDecodeError as err:
            with open(filepath, "r",encoding='utf-16-le')as tmp1:
                self.QPlainTextEdit_1.setText(tmp1.read())
            tmp1.close()

  
        
    def setRunbutton(self, vaule):
        self.pushButton_3.setDisabled(vaule)           
        #self.env_path, self.env_lib, self.env_inculde
    def setenv(self, event):
        win32api.MessageBox(0, "The apps is looking for vs folder,plase wait for a moment!", "Warring Message", win32con.MB_OK)
        strfilepath=''
        
        dirlist=[]
        if (self.radioButton_2.isChecked()==False):
            dirs=[f.path for f in os.scandir(rootdir) if f.is_dir() and f.path.find("Program F")>0]
            if len(dirs)>1:
                strfilepath = "c:\\Program Files (x86)\\"
            else:
                strfilepath= "c:\\Program Files\\"   
        else:
            strfilepath=self.lineEdit_2.text()
        dirlist +=[f.path for f in os.scandir(strfilepath) if f.is_dir() and f.path.find("Microsoft Visual Studio")>0]
        if len(dirlist)>0:
            for dir in dirlist:
                self.env_do(dir)
        else:
            win32api.MessageBox(0, "Folder"+str_err+"is not in "+strfilepath+"\\VC folder！Please make sure Visual Studio is instlled!", "Warring Message", win32con.MB_OK)
    
    
    def env_do(self,strfilepath ):
        print(strfilepath)
        env_path=self.env_path
        env_lib=self.env_lib
        env_include=self.env_include
        str_ide=''
        str_bin=''
        str_include=''
        str_lib=''
        status=0
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
#                         print('libfound!')
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
    
#        if(str_err):
#            win32api.MessageBox(0, "Folder"+str_err+"is not in "+strfilepath+"\\VC folder！Please make sure Visual Studio is instlled!", "Warring Message", win32con.MB_OK)
        print("str_err:"+str_err)
        if(str_err==''):
            win32api.MessageBox(0, "The apps is setting environment,plase wait for a moment!", "Warring Message", win32con.MB_OK)
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
            status+=1
 
        if(str_err=='' and os.path.isfile(strfilepath+'\\VC\\lib\\Kernel32.Lib')==False):
            print(strfilepath+'\\VC\\lib\\Kernel32.Lib')
            cpath=os.getcwd()+'\\Kernel32.Lib'
            if(os.path.isfile(cpath)):
                tpath=strfilepath+'\\VC\\lib\\Kernel32.Lib'
                try:
                    shutil.copyfile(cpath, tpath)
                    status+=1
                except Exception as err:
                    win32api.MessageBox(0, err, "PermissionError Message", win32con.MB_OK)
            else:
                win32api.MessageBox(0, "\'Kernel32.Lib\' file is not in the currect folder,please copy it to folder \'VC\\lib\'!", "Warring Message", win32con.MB_OK)
        else:
            status+=1
        print(status)
        if status==2:
            self.setRunbutton(False)
            win32api.MessageBox(0, "We have set environment variables for you,please restart the Apps", "Warring Message", win32con.MB_OK)
            sys.exit()

    def envok(self):
        self.pushButton_5.setVisible(False)
        self.radioButton.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.lineEdit_2.setVisible(False)
#        self.pushButton_6.setVisible(False)

 
    
if __name__ == "__main__":
    import sys
    env_path= os.getenv('PATH')
    env_lib=os.getenv('LIB')
    env_include=os.getenv('INCLUDE')
    env_ok=False
    rs_ide=''
    rs_bin=''
    rs_include=''
    rs_lib=''
    rootdir ='c:\\'

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
    
    if(rs_bin and os.path.exists(rs_bin) and rs_ide and os.path.exists(rs_ide) and rs_lib and os.path.exists(rs_lib) and rs_include and os.path.exists(rs_include)):
        print('Your computer do not need set environment')
        win32api.MessageBox(0,"Your computer doesn't need to set environment varialbes!", "Ok Message")
        strfilepath=rs_lib
        env_ok=True
        tpath=rs_lib+'\\Kernel32.Lib'
        if (os.path.isfile(tpath)==False):
            cpath=os.getcwd()+'\\Kernel32.Lib'
            try:
                shutil.copyfile(cpath, tpath)
            except Exception :
                win32api.MessageBox(0, "We haven't right to copy 'kernel132.lib' into 'xxx\Microsoft Visual Studio xx\VC\lib\' ,please copy it", "PermissionError Message", win32con.MB_OK)
    else:
        win32api.MessageBox(0,"Please set Visual Studio folder first!")
    
   
  
  
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.QPlainTextEdit_1.setLexer(QsciLexerCPP())
    if(rs_ide!='' and rs_bin!= '' and rs_include !='' and rs_lib!=''):
        
        if env_ok==False:
            ui.setRunbutton(True)
        else:
            ui.envok()
    Dialog.show()
    sys.exit(app.exec_())


