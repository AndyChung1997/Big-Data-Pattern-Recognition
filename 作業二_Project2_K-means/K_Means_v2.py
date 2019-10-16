# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:02:11 2019

@author: Andy Chung
"""
import numpy as np
import matplotlib.pyplot as plt
import operator
import random


# 兩條線之間的距離
def dist(x, y, tx, ty):
    return int(((tx-x)**2)**0.5)   


a = int(input("做幾個高斯分布圖? "))
dataset = []
count = 0
d=int(input("D = "))       #幾次做一個歸納?
n=int(input("N = "))       #重複幾次?
while True:
    p=int(input("probability is: "))
    
    r = [0 for n in range(d)]     
    avg = (p*0.01)*d
    std = ((p*0.01)*d*(1-p*0.01))**0.5
    
    for i in range(n):
        x = np.random.normal(avg,std,1)
        if (x[0] >= 0 and x[0] <= d):
            r[int(x)] = r[int(x)] + 1
            #print(r[int(x)])
        pr = int(x)
    for i in range(d):
        #print("%d , %d"%(i, r[i]))
        dataset.append([i,r[i]])
    #print(dataset)
    count += 1
    if (count == a):
        break

# the number of cluster centers        
c_num = int(input("幾個群集中心? "))

# data points
x = []
y = []
#print(type(dataset))   # type = "list"

for i in range(len(dataset)):
    if(int(dataset[i][1])) != 0:
        x.append(int(dataset[i][0]))
        y.append(int(dataset[i][1]))
             

plt.figure('Draw')
plt.axis([0, d, 0, max(y)+10])
plt.title("K-means")
plt.grid(b = True, color = 'lightgray')  #網格  
line2 = plt.gca()
for i in range(len(y)):
    line2.plot([x[i],x[i]],[0,y[i]],c='gray')   
plt.savefig('kmeans_org.png')
plt.show()
       

# 隨機取N個 cluster centers
kx = np.random.randint(0, len(x) , c_num)
ky = np.random.randint(0, 100 , c_num)

for i in range (c_num):                #避免 division by zero
    while(np.array(x[kx[i]]) == 0):
        kx[i] = random.randint(0,d)
       
        
# clustering
def cluster(x, y, tx, ty):
    group = []
    temp = []
    for i in range(c_num):
        group.append([])
        temp.append([])
    min_dist = 99999
    for i in range(len(x)):
        for j in range(c_num):
            distance = dist(x[i], y[i], tx[j], ty[j])
            #print("%d\t"%distance)
            if distance <= min_dist:
                min_dist = distance
                flag = j
        group[flag].append([x[i], y[i]])   # 分成N群
        temp[flag].append([x[i],0])
        min_dist = 99999
    return group , temp

# find new cluster centers
def new_center(group, tx, ty):
    sum_x = 0
    sum_y = 0
    new_c = []
    test = []
    
    for number, nodes in enumerate(group):   #enumerate(sequence, [start=0])，sequence -- 一個序列
        if (operator.eq(nodes,test)):
            new_c.append([kx[number],ky[number]])
        for node in nodes:
            sum_x = sum_x + node[0]    # x的值加總
            sum_y = sum_y + node[1]    # y的值加總
        new_c.append([int(sum_x/len(nodes)), int(sum_y/len(nodes))])  # 取平均值
        sum_x = 0
        sum_y = 0
    new_kx = []
    new_ky = []
    for i in new_c:
        new_kx.append(i[0])  #新的群集中心x
        new_ky.append(i[1])  #新的群集中心y
    return new_kx, new_ky

# k-means 分群
def k_means(x, y, kx, ky, pic):
    p , t = cluster(x, y, kx, ky)    #分類出來的群集
    
    nkx, nky = new_center(p, kx, ky)  #新的點
    plt.figure('Draw')
    plt.axis([0, d, 0, max(y)+10])
    plt.title("K-means")
    plt.grid(b = True, color = 'lightgray')  #網格    
    colors ="bgrcmyk"    # 七種顏色
    color_index = 0
    colors2 ="cmykbgr"   # 七種顏色
    color_index2 = 0
    for index , nodes in enumerate(p):
        # 繪圖
        for i in range(len(p[index])):           #第N群
            line = plt.gca()
            #  設定每一群的線條顏色
            line.plot([t[index][i][0],p[index][i][0]], [t[index][i][1],p[index][i][1]],c=colors[color_index])
            #  設定每一群集中心的顏色
            line.plot([kx[index],kx[index]],[0,max(y)+10],c=colors2[color_index2])   #群集中心
        color_index += 1
        color_index2 += 1 
    plt.savefig('kmeans_%s.png' % pic)
    plt.show()
    
    # cluster centers change or not?
    if nkx == list(kx) and nky == list(ky):
        return 0
    else:
        pic += 1
        k_means(x, y, nkx, nky, pic)

k_means(x, y, kx, ky, pic = 0)
