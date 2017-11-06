# coding: utf-8
'''
Created on 2017年11月7日

@author: raytine
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

简单字符串加法
如果使用python的库函数，先转成int在计算会更快
32.7%
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        a_length = len(a)
        b_length = len(b)
        if b_length > a_length:
            a, b = b, a
        a_length = len(a) - 1
        b_length = len(b) - 1
        up = 0
        for i in range(len(b)):
            add = int(a[a_length - i]) + int(b[b_length - i]) + up
            result.append(add%2)
            up = add/2
        length = a_length-b_length
        for i in range(length):
            add = int(a[length - i - 1]) + up
            result.append(add%2)
            up = add/2
        if up == 1:
            result.append(1)
        result.reverse()
        return ''.join([str(i) for i in result])

# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return bin(int(a, 2) + int(b, 2))[2:]