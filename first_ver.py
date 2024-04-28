import time,math,random,matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
from PIL import Image
from scipy.interpolate import interp1d
import numpy as np

background = plt.imread("攻打敵船背景.jpg")
我方船 = plt.imread("我方船.png")
我方香蕉船 = plt.imread("我方香蕉船.png")
敵方船 = plt.imread("敵方船.png")


我船船種 = input("請選擇：「a. 香蕉船」 或是 「b.商船」：")
if (我船船種 == "a" or "A"):
    我船 = 我方香蕉船
elif (我船船種 == "b" or "B"):
    我船 = 我方船
else:
    我船 = 我方船

船體長 = random.randint(20, 75)
距離 = random.randint(300,900)
砲彈數量 = 15
print("船離你的距離 =", 距離, "\n你現在有", 砲彈數量, "個砲彈")
    
    
    
def drowb():
    #fig = plt.figure(figsize=(10, 5), dpi=100)
    fig, BGI = plt.subplots(figsize=(10, 5))
    x = [0, ((射程)/2), 射程]
    x_new = np.linspace(1, x[2])
    y = [1, 最大高度, 1]
    f1 = interp1d(x, y, kind='quadratic')
    敵x = 距離
    敵y = y[0]
    x反應用 = []
    y反應用 = []

    x反射程 = 射程/2
    速度平方 = (((敵x - x反射程)*9.8)**2)**(1/2)
    y反中點 = 最大高度
    y反最高 = ((敵x - x反射程)**2/ 速度平方) * 9.8 / 2

    x反應用 = [x反射程, (敵x+x反射程)/2, 敵x]
    x反應用_new = np.linspace(x反應用[0], x反應用[2])
    y反應用 = [y反中點, y反最高, 敵y]          #陣列中第一個應為當時高度
    f2 = interp1d(x反應用, y反應用, kind='quadratic')
    
    敵x = [敵x]
    plt.plot(敵x, 敵y)
    #plt.yticks([])
    plt.plot(x, y, 'o', x_new, f1(x_new), '-')
    plt.plot(x反應用, y反應用, 'o', x反應用_new, f2(x反應用_new), '-')    
    plt.xticks(ticks=(敵x), labels=敵x, color='r', fontsize=20,)
    if 射程>距離:
        BGI.imshow(background, extent = [-50, 射程+50, 0, (射程/2)+50])
        plt.axes([ 50/(敵x[0]), 0.15, 0.1, 0.1 ])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(我船)
        plt.axes([ (敵x[0]/射程)-0.167, 0.15, 0.1, 0.1 ])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(敵方船)
    else:
        BGI.imshow(background, extent = [-50, (敵x[0]+50), 0, (距離/2)+50])
        plt.axes([ 50/(敵x[0]), 0.15, 0.1, 0.1 ])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(我船)
        plt.axes([ (敵x[0]/(敵x[0]+50))-0.095, 0.15, 0.1, 0.1 ])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(敵方船)
    plt.show()
            
def drown():
    figure, BGI = plt.subplots(figsize=(10, 5))
    x = [1, ((射程)/2), 射程]
    x_new = np.linspace(1, x[2])
    y = [70, 最大高度+70, 70]
    f1 = interp1d(x, y, kind='quadratic')

    敵x = 距離
    敵y = y[0]
    敵x = [敵x]
    plt.plot(敵x, 敵y)
    #plt.yticks([])
    plt.plot(x, y, 'p', x_new, f1(x_new), '-')
    plt.xticks(ticks=(敵x), labels=敵x, color='g', fontsize=20,)
    if 射程>距離:
        BGI.imshow(background, extent = [-50, 射程+50, 0, (射程/2)+50])
        plt.axes([ 50/(敵x[0]), 0.15, 0.1, 0.1 ])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(我船)
        plt.axes([ (敵x[0]/射程)-0.167, 0.15, 0.1, 0.1 ])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(敵方船)
    else:
        BGI.imshow(background, extent = [-50, (敵x[0]+50), 0, (距離/2)+50])
        plt.axes([ 50/(敵x[0]), 0.15, 0.1, 0.1 ])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(我船)
        plt.axes([ (敵x[0]/(敵x[0]+50))-0.095, 0.15, 0.1, 0.1 ])
        plt.xticks([])
        plt.yticks([])
        plt.imshow(敵方船)
    plt.show()    


while True:
    速度 = float(input("請輸入速度: "))
    角度 = float(input("請輸入角度: "))
    射程 = (((速度*速度) * (math.sin(math.degrees(角度*2))) / 9.8)**2)**(0.5)
    最大高度 = 速度*速度* ((math.sin(math.degrees(角度)))*(math.sin(math.degrees(角度))) / (2*9.8))
        
    if (角度>90) or (角度==0) or (角度<0) or (速度==0):
        print("是不是想找BUG？可惜沒有\n")
        break
    elif (速度>10000000):
        print("這是要上月球的速度吧？！？！")
        break
    if 射程 == 0.0:
        print("你不幸炸到自己了")
        break    
    
    if ((距離+1) > 射程 > 距離) or (距離+船體長) < 射程 <(距離+船體長+1):
        反導 = random.randint(0, 1)
        砲彈數量 -= 1
        if 反導 == 0:
            print("擦船而過,目前船與你的距離為", 距離, "\n剛剛的砲彈射程為", 射程, "\n目前你還有", 砲彈數量, "發")
            drown()
        else:
            print("理論上砲彈會擦過對方船身，但是你的砲彈被反了")
            drowb()
    elif (距離+船體長) > 射程 > (距離-船體長):
        反導 = random.randint(0, 1)
        if 反導 == 1:
            print("理論上會打中，但是你的砲彈被反了", 距離, "\n剛剛的砲彈射程為", 射程, "\n目前你還有", 砲彈數量, "發")
            drowb()
        else:
            print("打中了，該船已沉\n", "\n剛剛的砲彈射程為", 射程)
            drown()
            是否再玩 = input("想再玩一次請輸入想：")
            if 是否再玩 == "想":
                pass
                距離 = random.randint(100,1000)   #單位m
                砲彈數量 = 15
                print("目前船與你的距離為{:.2f}".format(距離), "\n目前你還有{:.2f}發".format(砲彈數量))
            else:
                break
    else:
        砲彈數量 -= 1
        反導 = 0
        print("技術頗爛，沒打中,目前船與你的距離為", 距離, "\n剛剛的砲彈射程為", 射程, "\n目前你還有", 砲彈數量, "發")
        drown()
    if (砲彈數量 == 0):
        print("沒砲了")
        break
