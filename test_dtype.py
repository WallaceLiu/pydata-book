from numpy import *

# N维数组对象ndarray，它是一系列同类型数据的集合，以0下标为开始进行集合中元素的索引。
import numpy as np

# 使用标量类型
dt = np.dtype(np.int32)
print(dt)

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)

# 字节顺序标注
dt = np.dtype('<i4')
print(dt)

# 将数据类型应用于 ndarray 对象
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)

# 类型字段名可以用于存取实际的 age 列
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])

#
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
