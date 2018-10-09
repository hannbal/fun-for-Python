import time
class schoolcalendar():
    __datelist=[]
#    room={1:'',2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:''}
    def makedatelist(self, startdate, weeks):
        stime=time.mktime(time.strptime(startdate, '%Y%m%d'))
        countdays=weeks*7
        for i in range(countdays):
            self.__datelist.append([stime+i*3600*24, {1:'',2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:''}, {1:'',2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:''}, {1:'',2:'', 3:'', 4:'', 5:'', 6:'', 7:'', 8:''}])
    
    def setcourse(self, num, coursename, weeks, room, wday):
        #num is a list of class's serial number ,weeks is a list of  weeks'serial number  wday is a list
        checklist=[]
        for i in weeks:
            for j in wday:
                for k in num:
                    if self.datelist[(i-1)*7+j][room][k]!='':
                        checklist.append((i,j,k,  self.datelist[(i-1)*7+j][room][k] ))
        if len(checklist)==0:
            for i in weeks:
                for j in wday:
                    for k in num:
                        self.datelist[(i-1)*7+j][room][k]=coursename
        else:
            return checklist
            
    def setdatelist(self, list):
        self.__datelist=list
        
    def getdatelist(self):
        return self.__datelist
    
    def delcourse(self, num,  weeks, room, wday):
        for i in weeks:
            for j in wday:
                for k in num:
                    self.datelist[(i-1)*7+j][room][k]=''
#        weeks=weeks.split(',')
#        count=0
#        week_list=[]
#        while len(weeks)>count:
#            if weeks[count].isnumeric():
#                week_list.append(int(weeks[count]))
#                count+=1
#            elif weeks[count].find('-'):
#                tmp = weeks[count].split('-')
#                if len(tmp)==2 and tmp[0].isnumeric() and tmp[1].isnumeric():
#                    for i in range(int(tmp[0]), 1+int(tmp[1])):
#                        week_list.append(i)
#                    count+=1
#            else:
#                print('err count:', weeks[count])
#                count+=1
#                
#                
#        tmp_num = num.split('-')
#        for i in week_list:
#            checknone=[]
#            for j in range(int(tmp_num[0]), int(tmp_num[1])+1):
#                if self.datelist[(i-1)+wday][room][j]=='':
#                    checknone.append(j)
#                    
#            self.datelist[(i-1)+wday][room].add({j:coursename})
            
        
        pass
    
    def wrtielisttotxt(self, path):
        with open(path, 'w')as tmp:
            tmp.write(str(self.__datelist))

def transformtime(timestr):
    list_time=[]
    if timestr.isnumeric():
        list_time.append(int(timestr))
    elif timestr.find(',')>0:
        substr = timestr.split(',')
        count=0
        for i in substr:
            tmp=transformtime(i)
            list_time[count:]=tmp
            count+=len(tmp)
    elif timestr.find('-')>0:
        substr=timestr.split('-')
        for i in range(int(substr[0]), int(substr[1])+1):
            list_time.append(transformtime(str(i))[0])
    else:
        return ('err', timestr)
    list_time.sort()
    return list_time





#test_2018 =schoolcalendar()
#test_2018.makedatelist('20180901', 23)
#test_2018.setcourse([1,2,3],'autocad',[1,2,3,4,5,6,9,10,13,14],1,[4])
#d=test_2018.getdatelist()
#	tmp.write(str(d))
#    
#test_2018.setcourse([1,2,3],'c++',[1,12,14],1,[4])
#transformtime('20,1-3,6-10,13,15,11-12')
