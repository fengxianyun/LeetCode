# coding: utf-8
'''
Created on 2017年11月9日

@author: raytine
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        save = set()
        result = []
        for num in nums:
            if num in save:
                result.append(num)
            else:
                save.add(num)
        return result
        