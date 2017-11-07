# coding: utf-8
'''
Created on 2017-11-7

@author: raytine
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

将罗马数字转换为数字范围从1-3999
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        save = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        temp = 0
        before = -1
        for i in s:
            i = save[i]
            if before == -1:
                temp = i
            elif before == i:
                temp += i
            elif before > i:
                result += temp
                temp = i
            else:
                result -= temp
                temp = i
            before = i
        result += temp
        return result
a = Solution()
a.romanToInt("DCXXI")