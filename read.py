import pickle
import numpy as np


# pathname = "E:\\脑电python3\\截取后数据\\s01\\s01-1.dat"
pathname = "E:\\DEAP数据集python\\处理后数据\\s01\\s01-1.dat"
# pathname = "E:\\脑电python3\\分频段后数据\\s01\\s01-1.dat"
# pathname = "E:\\脑电python3\\PCC矩阵\\s01\\s01-1.dat"
# pathname = "E:\\脑电python3\\二值矩阵\\s01\\s01-1.dat"
# pathname = "E:\\脑电python3\\网络属性\\s01\\s01-1.dat"
# pathname = "E:\\脑电python3\\分类处理数据\\s01\\s01-1.dat"
# pathname = "E:\\脑电python3\\分类再处理数据\\deap2.dat"
# pathname = "E:\\脑电python3\\分类再处理数据\\deap2_avg.dat"
fp = open(pathname, "rb")
x = pickle.load(fp)
print(x)
print('------------------')
# xx = x['Theta']
# print(xx)
# print(len(xx))
print('------------------')
xxx = x['data']
print(xxx)
print(len(xxx))
print(xxx.shape)
print('------------------')
label = x['labels']
print(label)