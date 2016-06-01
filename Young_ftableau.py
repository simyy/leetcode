#!/usr/bin/env python
# encoding: utf-8

“”“
杨氏矩阵查找元素方法
1. 遍历
2. 二分法遍历
3. 线性搜索利用有序关系，右上角的特性：大于左侧并小于下侧
”“”


class Point:
    """
    坐标点
    |---> x
    |
    v y
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


def binary_search(data, x):
    '''二分法查找
    找到不满足x大小的范围
    @return -1: 全部都不满足
             i: 二分法结果
    '''
    if not data:
        return -1
    i = 0
    j = len(data) - 1
    while i < j:
        m = i + (j - i) / 2 # 防止越界
        if data[m] > x:
            j = m - 1
        elif data[m] < x:
            i = m + 1
        else:
            return m
    if data[i] > x:
        return i - 1
    return i


def find_loop(data, point1, point2, x):
    '''递归遍历
    @data 输入矩阵，利用矩阵左上角和右下角来确定矩阵范围
    @point1 矩阵左上顶点
    @point2 矩阵右下顶点
    @x 目标值
    '''
    # 矩阵不成立，左上角已经大于右下角的坐标值
    if point1.x > point2.x or point1.y > point2.y:
        return False
    
    # 沿x轴二分查找
    n = binary_search(data[point1.y][point1.x:point2.x+1], x)
    if n == -1: # 不在范围内，失败
        return False
    elif data[point1.y][point1.x+n] == x: # 如果当前节点为目标值，成功
        return True
    point2.x = point1.x + n # 调整矩阵大小

    # 沿y轴二分查找
    tmp = [d[point1.x] for d in data[point1.y:]]
    n = binary_search(tmp, x)
    if n == -1: # 不在范围内，失败
        return False
    elif data[point1.y+n][point1.x] == x: # 如果当前节点为目标值，成功
        return True
    point2.y = point1.y + n # 调整矩阵大小

    # 由于二分查找过程已经遍历过上和左侧的数据，所以需要移动参考顶点
    point1.x += 1
    point1.y += 1

    return find_loop(data, point1, point2, x)


def find(data, x):
    '''利用二分法在有序矩阵中查找数字
    '''
    # 如果输入为空，则查找失败
    if not data or not data[0]:
        return False
    # 初始化矩阵参考点
    point1 = Point(0, 0)
    point2 = Point(len(data) - 1, len(data[0]) - 1)
    return find_loop(data, point1, point2, x)


def linear_search(data, d):
    max_row = len(data) - 1
    max_column = len(data[0]) - 1

    i = 0 
    j = max_column
    while i <= max_row and j >= 0:
        if data[i][j] > d:
            j -= 1
        elif data[i][j] < d:
            i += 1
        else:
            return True
    return False


if __name__ == '__main__':
    data = [[1, 2, 3],
            [3, 4, 6],
            [9, 12, 18]]
    print '矩阵为：'
    for d in data:
        print ' '.join([str(x) for x in d])

    print 
    print '测试数据：'
    for x in [1, 2, 3, 4, 6, 9, 12, 18]:
        print 'find %s, result: %s' % (x, find(data, x))
    
    for x in [0.3, 1.3, 3.1, 6.1, 8.1, 18.1]:
        print 'find %s, result: %s' % (x, find(data, x))

    data = [0]
    for i in [-1, 0, 1]:
        print 'binary_search %s : ' % i,  binary_search(data, i)

    print
    data = [[1, 2, 3],
            [3, 4, 6],
            [9, 12, 18]]
    print 
    print '测试数据：'
    for x in [1, 2, 3, 4, 6, 9, 12, 18]:
        print 'linear_search %s, result: %s' % (x, linear_search(data, x))
    
    for x in [0.3, 1.3, 3.1, 6.1, 8.1, 18.1]:
        print 'linear_search %s, result: %s' % (x, linear_search(data, x))
