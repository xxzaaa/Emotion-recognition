import pickle
import numpy as np


pathname = "E:\\DEAP数据集python\\处理后数据\\s01\\"
tensor = []
for j in range(0, 40):
    # if (i + 1) < 10:
    filename = "s01-%d.dat" % ((j + 1))
    # if (i + 1) >= 10:
    #     filename2 = "s%d-%d.dat" % ((i + 1), (j + 1))
    s = open(pathname + filename, "rb")  # 以bytes类型正常读取文件
    x = pickle.load(s, encoding="latin1")
    tensor.append(x['data'])
# print(len(tensor))
# print(tensor[0])


w = np.array([tensor[0], tensor[1], tensor[2], tensor[3], tensor[4],
              tensor[5], tensor[6], tensor[7], tensor[8], tensor[9],
              tensor[10], tensor[11], tensor[12], tensor[13], tensor[14],
              tensor[15], tensor[16], tensor[17], tensor[18], tensor[19],
              tensor[20], tensor[21], tensor[22], tensor[23], tensor[24],
              tensor[25], tensor[26], tensor[27], tensor[28], tensor[29],
              tensor[30], tensor[31], tensor[32], tensor[33], tensor[34],
              tensor[35], tensor[36], tensor[37], tensor[38], tensor[39],
              ])
print(w.ndim)
print(w)

# w = np.array([[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]])
