# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:26:10 2019

@author: TonyLin
"""
import copy
a=[]
for x in range(0, 9):
    a.append([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
a[0][0]=[8]
a[0][1]=[1,2,3,4,5,6,7,8,9]
a[0][2]=[4]
a[0][3]=[6]
a[0][4]=[1,2,3,4,5,6,7,8,9]
a[0][5]=[1,2,3,4,5,6,7,8,9]
a[0][6]=[1,2,3,4,5,6,7,8,9]
a[0][7]=[1,2,3,4,5,6,7,8,9]
a[0][8]=[3]

a[1][0]=[1,2,3,4,5,6,7,8,9]
a[1][1]=[1,2,3,4,5,6,7,8,9]
a[1][2]=[1,2,3,4,5,6,7,8,9]
a[1][3]=[1,2,3,4,5,6,7,8,9]
a[1][4]=[1,2,3,4,5,6,7,8,9]
a[1][5]=[1]
a[1][6]=[1,2,3,4,5,6,7,8,9]
a[1][7]=[1,2,3,4,5,6,7,8,9]
a[1][8]=[1,2,3,4,5,6,7,8,9]

a[2][0]=[1,2,3,4,5,6,7,8,9]
a[2][1]=[1,2,3,4,5,6,7,8,9]
a[2][2]=[9]
a[2][3]=[5]
a[2][4]=[1,2,3,4,5,6,7,8,9]
a[2][5]=[1,2,3,4,5,6,7,8,9]
a[2][6]=[7]
a[2][7]=[1,2,3,4,5,6,7,8,9]
a[2][8]=[1]

a[3][0]=[1,2,3,4,5,6,7,8,9]
a[3][1]=[4]
a[3][2]=[1,2,3,4,5,6,7,8,9]
a[3][3]=[1,2,3,4,5,6,7,8,9]
a[3][4]=[1,2,3,4,5,6,7,8,9]
a[3][5]=[1,2,3,4,5,6,7,8,9]
a[3][6]=[5]
a[3][7]=[1,2,3,4,5,6,7,8,9]
a[3][8]=[8]

a[5][0]=[6]
a[5][1]=[1,2,3,4,5,6,7,8,9]
a[5][2]=[7]
a[5][3]=[1,2,3,4,5,6,7,8,9]
a[5][4]=[1,2,3,4,5,6,7,8,9]
a[5][5]=[1,2,3,4,5,6,7,8,9]
a[5][6]=[1,2,3,4,5,6,7,8,9]
a[5][7]=[2]
a[5][8]=[1,2,3,4,5,6,7,8,9]

a[6][0]=[3]
a[6][1]=[1,2,3,4,5,6,7,8,9]
a[6][2]=[8]
a[6][3]=[1,2,3,4,5,6,7,8,9]
a[6][4]=[1,2,3,4,5,6,7,8,9]
a[6][5]=[2]
a[6][6]=[9]
a[6][7]=[1,2,3,4,5,6,7,8,9]
a[6][8]=[1,2,3,4,5,6,7,8,9]

a[7][1]=[1,2,3,4,5,6,7,8,9]
a[7][1]=[1,2,3,4,5,6,7,8,9]
a[7][3]=[9]
a[7][4]=[1,2,3,4,5,6,7,8,9]
a[7][5]=[1,2,3,4,5,6,7,8,9]
a[7][6]=[1,2,3,4,5,6,7,8,9]
a[7][7]=[1,2,3,4,5,6,7,8,9]
a[7][8]=[1,2,3,4,5,6,7,8,9]

a[8][0]=[7]
a[8][1]=[1,2,3,4,5,6,7,8,9]
a[8][2]=[1,2,3,4,5,6,7,8,9]
a[8][3]=[1,2,3,4,5,6,7,8,9]
a[8][4]=[1,2,3,4,5,6,7,8,9]
a[8][5]=[4]
a[8][6]=[3]
a[8][7]=[1,2,3,4,5,6,7,8,9]
a[8][8]=[5]

def twinschenck(apple):
    changed=0
    cnt = count(apple)
#    print(cnt)
    tmp2=[]
    for x in cnt:
        if x[0]==2:
            tmp2.append(x)
#    print(tmp2)
#    print(tmp2[1:])
    for x in range(0, len(tmp2)):
        for y in range(x+1, len(tmp2)):
            if tmp2[x][1]==tmp2[y][1] and apple[tmp2[x][1]][tmp2[x][2]]==apple[tmp2[y][1]][tmp2[y][2]]:
#                print (x, y, tmp2[x], tmp2[y])
                for i in apple[tmp2[x][1]]:
                    for z in  apple[tmp2[x][1]][tmp2[x][2]]:
                        if z in i and i!=apple[tmp2[x][1]][tmp2[x][2]]:
                            i.remove(z)
                            changed+=1
#                print (x, y, tmp2[x], tmp2[y])
            if tmp2[x][2]==tmp2[y][2]:
                if tmp2[x][2]==tmp2[y][2] and apple[tmp2[x][1]][tmp2[x][2]]==apple[tmp2[y][1]][tmp2[y][2]]:
#                            print (x, y, tmp2[x], tmp2[y])
                    for j in range(0, 9):
                        if j !=tmp2[x][1] and j!=tmp2[y][1]:
                            for z in apple[tmp2[x][1]][tmp2[x][2]]:
                                if z in apple[j][tmp2[x][2]]:
                                    apple[j][tmp2[x][2]].remove(z)
                                    changed+=1
            if int(tmp2[x][1]/3)==int(tmp2[y][1]/3) and int(tmp2[x][2]/3) == int(tmp2[y][2]/3) and apple[tmp2[x][1]][tmp2[x][2]]==apple[tmp2[y][1]][tmp2[y][2]] :
                for k in range(0, 9):
                    if apple[3*int(tmp2[x][1]/3)+int(k/3)][3*int(tmp2[x][2]/3)+k%3] != apple[tmp2[x][1]][tmp2[x][2]] :
                        for z in apple[tmp2[x][1]][tmp2[x][2]]:
                            if z in apple[3*int(tmp2[x][1]/3)+int(k/3)][3*int(tmp2[x][2]/3)+k%3]:
#                                print(tmp2[x], tmp2[y])
#                                print(x, y, apple[3*int(tmp2[x][1]/3)+int(k/3)][3*int(tmp2[x][2]/3)+k%3], z, 3*int(tmp2[x][1]/3)+int(k/3), 3*int(tmp2[x][2]/3)+k%3)
                                apple[3*int(tmp2[x][1]/3)+int(k/3)][3*int(tmp2[x][2]/3)+k%3].remove(z)
                                changed+=1
    return changed                        
    
    
    
def __filter_(apple):
    
    check_change=1
    while(check_change):
        check_change=0
        #行列9格中存在只有一个可能的数，对同行列9格过滤
        for aa in apple:
            for t in aa:
                if len(t)==1:
                    x=apple.index(aa)
                    y=aa.index(t)
                    
                    for i in range(0,9):
                        if i!=y and t[0] in apple[x][i]:
                            apple[x][i].remove(t[0])
                            check_change=1
                        if t==[]:
                            return apple

                        if i!=x and t[0] in apple[i][y]:
                            apple[i][y].remove(t[0])
                            check_change=1
                    xx=int(x/3)
                    yy=int(y/3)
                    for i in range (0,3):
                        for ii in range(0,3):
                            if (i+3*xx)!=x or (ii+3*yy)!=y: 
                                if t[0] in apple[i+3*xx][ii+3*yy]:
                                    #if t[0]==4:
                                     #   print(x,y,i+3*xx,ii+3*yy,i,ii,xx,yy)
                                    apple[i+3*xx][ii+3*yy].remove(t[0])
                                    check_change=1
                                    
        for i in range(0, 9):
            z=rowcheck(apple[i])
            if len(z)<9:
                for aa in apple[i]:
                    if len(aa)>1:
                        for zz in z:
                            if zz in aa and len(aa)>1:
                                apple[i][apple[i].index(aa)]=[zz]
                                check_change=1
                        
        for i in range(0, 9):
            tmp=[] 
            for t in range(0, 9):
                tmp.append(apple[t][i])
            z=rowcheck(tmp)
#            print("tmp:", tmp)
            for t in range(0, 9):
                if len(apple[t][i])>1:
                    for zz in z:
                        if zz in apple[t][i]:
                            apple[t][i]=[zz]
                            check_change=1
        check_change+=twinschenck(apple)   
#        cnt = count(apple)
#    print(cnt)
#    tmp2=[]
#    for x in cnt:
#        if x[0]==2:
#            tmp2.append(x)
##    print(tmp2)
##    print(tmp2[1:])
#        for tx in range(0, len(tmp2)-1):
#            for ty in range(tx+1, len(tmp2)):
#                if tmp2[tx][1]==tmp2[ty][1] and apple[tmp2[tx][1]][tmp2[tx][2]]==apple[tmp2[ty][1]][tmp2[ty][2]]:
##                    print (x, y, tmp2[x], tmp2[y])
#                    for i in apple[tmp2[tx][1]]:
#                        for z in apple[tmp2[tx][1]][tmp2[tx][2]]:
#                            if z in i and i!=apple[tmp2[tx][1]][tmp2[tx][2]]:
#                                i.remove(z)
#                                check_change+=1
##                print (x, y, tmp2[x], tmp2[y])
#                if tmp2[tx][2]==tmp2[ty][2] and apple[tmp2[tx][1]][tmp2[tx][2]]==apple[tmp2[ty][1]][tmp2[ty][2]]:
##                       print (x, y, tmp2[x], tmp2[y])
#                    for j in range(0, 9):
#                        if j !=tmp2[tx][1] and j!=tmp2[ty][1]:
#                            for z in apple[tmp2[tx][1]][tmp2[tx][2]]:
#                                if z in apple[j][tmp2[tx][2]]:
#                                    apple[j][tmp2[tx][2]].remove(z)
#                                    check_change+=1
    return(apple)               

            


def count(apple):
    cnt1=[]
    row=0
    for x in apple:
        col=0    
        for y in x:
            if len(y)>1:
                cnt1.append( [len(y),apple.index(x, row),x.index(y, col)] )
            col=col+1
        row=row+1
    cnt1.sort()
    return cnt1

        
def rowcheck(apple):
    z=[]
    alone=[]
    for x in apple:
        z+=x
    for i in range(1, 10):
        if z.count(i)==1:
            alone.append(i)
    return alone
    
       

def loop2filter(apple):
    error=0
    cnt = count(apple)
    while len(cnt)>0:
        for x in range(0, len(cnt)):
            for y in apple[cnt[x][1]][cnt[x][2]]:
                tmp = copy.deepcopy(apple)
                tmp[cnt[x][1]][cnt[x][2]]=[y]
                __filter_(tmp)
                for i in tmp:
                    for j in i:
                        if j==[]:
                            error=1
                            break
                    if error == 1:
                        break
                if error>0:
                    tmp = copy.deepcopy(apple)
                    if apple[cnt[x][1]][cnt[x][2]].index(y)<len(apple[cnt[x][1]][cnt[x][2]]):
                        error=0
                        continue
                    else:
                        break
                elif error==0 :
                    if len(count(tmp))>1:
                        tmp = loop2filter(tmp)

                    else:
                        apple=tmp
                        return tmp
                
                
    return apple            
    


a=__filter_(a)
k=17
for i in range(0, 9):
    print("")
    for j in range(0, 9):
        str="                 "
        print(a[i][j], str[:(k-(len(a[i][j])-1)*3)-1], end="")
print("")

a= loop2filter(a)
k=17
for i in range(0, 9):
    print("")
    for j in range(0, 9):
        str=" "
        print(a[i][j],str, end="")
print("")


