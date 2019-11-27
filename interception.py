import pickle
import numpy as np
import os
# 数据的截取
# 32个人，每个人的40次实验分成40个文件保存
# 去掉3秒基线后，对60秒的数据，截取中间20s进行实验
# 将这20s的数据分成4个5s，每个data为32*640
pathname1 = "E:\\DEAP数据集python\\data_preprocessed_python\\"
pathname3 = "E:\\DEAP数据集python\\处理后数据\\"

for i in range(0, 32):
    if (i+1) < 10:
        filename1 = "s0%d.dat" % (i+1)
    if (i+1) >= 10:
        filename1 = "s%d.dat" % (i+1)
    print(pathname1 + filename1)
    s = open(pathname1 + filename1, "rb")
    x = pickle.load(s, encoding="latin1")   # x为字典，键是'data'和'labels'，值是列表
    data1 = x['data']
    labels1 = x['labels']
    data2 = np.array(data1)
    labels2 = np.array(labels1)
    if (i+1) < 10:
        pathname2 = "s0%d\\" % (i+1)
    if (i+1) >= 10:
        pathname2 = "s%d\\" % (i+1)
    pathname4 = pathname3 + pathname2
    if not os.path.exists(pathname4):   # 创建文件夹
        os.mkdir(pathname4)

    for j in range(0, 40):
        data31 = data2[j, 0:32, (3 * 128 + 1):(63 * 128 + 1)]
        # data31 = data2[j, 0:32, (24 * 128 + 1):(29 * 128 + 1)]
        # data32 = data2[j, 0:32, (29 * 128 + 1):(34 * 128 + 1)]
        # data33 = data2[j, 0:32, (34 * 128 + 1):(39 * 128 + 1)]
        # data34 = data2[j, 0:32, (39 * 128 + 1):(44 * 128 + 1)]
        labels3 = labels2[j, :]

        if labels3[0] > 5:      # 给valence加标签
            labels3 = np.append(labels3, 2)
        else:
            labels3 = np.append(labels3, 1)
        if labels3[1] > 5:      # 给arousal加标签
            labels3 = np.append(labels3, 2)
        else:
            labels3 = np.append(labels3, 1)

        if (i+1) < 10:
            filename2 = "s0%d-%d.dat" %((i+1), (j+1))
        if (i+1) >= 10:
            filename2 = "s%d-%d.dat" %((i+1), (j+1))
        dict1 = {'data': data31,  'labels': labels3}    # 把数据保存成字典
        # dict1 = {'data1': data31, 'data2': data32, 'data3': data33,
        #          'data4': data34, 'labels': labels3}    # 把数据保存成字典

        fp = open(pathname4 + filename2, 'wb')
        pickle.dump(dict1, fp)
        fp.close()