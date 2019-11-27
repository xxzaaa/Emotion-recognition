import pickle
import numpy as np


pathname = "E:\\DEAP数据集python\\处理后数据\\s01\\"
# fp = open(pathname, "rb")
# x = pickle.load(fp)
# label = x['labels']
# print(label)
tensor = []
for j in range(0, 40):
    # if (i + 1) < 10:
    filename = "s01-%d.dat" % ((j + 1))
    # if (i + 1) >= 10:
    #     filename2 = "s%d-%d.dat" % ((i + 1), (j + 1))
    s = open(pathname + filename, "rb")  # 以bytes类型正常读取文件
    x = pickle.load(s, encoding="latin1")
    label = x['labels']
    print(label)
    tensor.append(x['data'])
# print(len(tensor))
# print(tensor[0])

