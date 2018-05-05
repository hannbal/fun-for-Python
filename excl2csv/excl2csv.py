import xlrd
import readdir
def readsheet(sheets, cols1, cols2):
    cols3   =[]
    cols4   =[]
    ncol1=0
    ncol3=0
    ncol4=0
    ncol1 = getid(sheets, ncol1,"学号" )    
    ncol3 = getid(sheets, ncol3,"课程名称" )    
    ncol4 = getid(sheets, ncol4,"教师" )    
    
    getcol(sheets, ncol1, cols1 )
    getcol(sheets, ncol4, cols4)
    getcol(sheets, ncol3, cols3)
    listjoin(cols2, cols3, cols4)
    
def listjoin(list1, list2, list3):
    i=0

    while i<len(list2):
        list1.append(list2[i]+list3[i]) 
        i +=1

def wirtetocsv(cols1, cols2, str, filename, path):
    file =path+"/"+filename+'.txt'
    with open(file, 'w')as tmp1:
        tmp1.write('')
    i=0
    while i< len(cols1):
        with open(file, 'a') as tmp2:
            tmp2.write(str+','+cols2[i].replace(',', '')+','+cols1[i].replace(',', '')+',\n')
            i+=1
    
def getid(sheets, ncol, str):
    i = 0
    while i<=sheets.ncols:
        if sheets.cell_value(rowx=0, colx=i).replace(' ','')== str:
            return i
        i += 1
    
def getcol(sheets, ncol, cols):
    i = 1
    j = 0
    while i<sheets.nrows:
        cols.append(sheets.cell_value(rowx=i, colx=ncol))
#        print("j="+str(j)+",value="+str(cols[j]))
        i +=1
        j += 1
#__booklist__

booklist=[]
path = "D:/Tony/python"
readdir.readdir(path, booklist)

for file_name in booklist:
    fullpath= path+"/"+file_name
    __mybook__ = xlrd.open_workbook(fullpath)
    __mysheet__ = __mybook__.sheet_by_index(0)
    __cols1__ =[]
    __cols2__ =[]
    readsheet(__mysheet__, __cols1__, __cols2__)
    wirtetocsv(__cols1__, __cols2__, "选修17-18下", file_name, path)
print(booklist)
