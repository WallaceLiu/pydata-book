from numpy import *

# N维数组对象ndarray，它是一系列同类型数据的集合，以0下标为开始进行集合中元素的索引。
import numpy as np

a = np.array([1, 2, 3])
print('一维')
print(a)

a = np.array([[1, 2], [3, 4]])
print('多于一维')
print(a)

a = np.array([1, 2, 3, 4, 5], ndmin=2)
print('最小维度')
print(a)

a = np.array([1, 2, 3], dtype=complex)
print('dtype 参数 ')
print(a)
