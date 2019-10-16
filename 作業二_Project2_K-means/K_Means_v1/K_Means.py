# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

# 兩點之間的距離
def dist(x, y, tx, ty):
    return int(((tx-x)**2)**0.5)   #  + (ty-y)**2)


myXY = np.loadtxt('case3.txt', delimiter='\t')
#print(myXY)

c_num = 2   # the numbers of cluster center         

plt.figure('Draw')
plt.axis([0, 100, 0, 100])
# data points
x = []
y = []
for i in range(len(myXY)):
    if(int(myXY[i,1])) != 0:
        x.append(int(myXY[i,0]))
        y.append(int(myXY[i,1]))
        #plt.scatter(x, y , c = 'gray')

# 隨機取兩個 cluster centers
kx = np.random.randint(0, 100 , c_num)
ky = np.random.randint(0, 100 , c_num)


# clustering
def cluster(x, y, tx, ty):
    group = [[],[]]
    temp = [[],[]]
    min_dist = 99999
    for i in range(len(x)):
        for j in range(c_num):
            distance = dist(x[i], y[i], tx[j], ty[j])
            #print("%d\t"%distance)
            if distance <= min_dist:
                min_dist = distance
                flag = j
        group[flag].append([x[i], y[i]])   # 分成兩群
        temp[flag].append([x[i],0])
        min_dist = 99999
    return group , temp

# find new cluster centers
def new_center(group, tx, ty):
    sum_x = 0
    sum_y = 0
    new_c = []
    for number, nodes in enumerate(group):   #enumerate(sequence, [start=0])，sequence -- 一個序列
        for node in nodes:
            sum_x = sum_x + node[0]    # x的值加總
            sum_y = sum_y + node[1]    # y的值加總
        new_c.append([int(sum_x/len(nodes)), int(sum_y/len(nodes))])  # 取平均值
        sum_x = 0
        sum_y = 0
    new_kx = []
    new_ky = []
    for i in new_c:
        new_kx.append(i[0])  #新的群集中心1
        new_ky.append(i[1])  #新的群集中心2
    return new_kx, new_ky

# k-means 分群
def k_means(x, y, kx, ky, pic):
    p , t = cluster(x, y, kx, ky)    #分類出來的群集
    
    nkx, nky = new_center(p, kx, ky)  #新的點
    plt.figure('Draw')
    plt.axis([0, 100, 0, 100])
    for i in range(len(p[0])):           #第一群
        #plt.scatter(p[0][i][0], p[0][i][1], c = 'r')
        line = plt.gca()
        line.plot([t[0][i][0],p[0][i][0]], [t[0][i][1],p[0][i][1]], color='r')
 
    
    for i in range(len(p[1])):           #第二群
        #plt.scatter(p[1][i][0], p[1][i][1], c = 'orange')
        line = plt.gca()
        line.plot([t[1][i][0],p[1][i][0]], [t[1][i][1],p[1][i][1]], color='orange')

        
    # 繪圖
    line = plt.gca()
    line.plot([kx[0],kx[0]],[0,100], color = 'b')
    #plt.scatter(kx[0], ky[0] , c = 'b', marker = '*')   #群集中心的初始點1
    line.plot([kx[1],kx[1]],[0,100], color = 'g')
    #plt.scatter(kx[1], ky[1] , c = 'b', marker = '^')   #群集中心的初始點2
    #plt.scatter(np.array(nkx[0]), np.array(nky[0]), c = 'g', marker = '*')  #新的群集中心1
    #plt.scatter(np.array(nkx[1]), np.array(nky[1]), c = 'g', marker = '^')  #新的群集中心2
    plt.show()
    
    # cluster centers change or not?
    if nkx == list(kx) and nky == list(ky):
        return 0
    else:
        pic += 1
        k_means(x, y, nkx, nky, pic)

k_means(x, y, kx, ky, pic = 0)


