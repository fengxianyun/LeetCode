# coding: utf-8
'''
Created on 2017年11月1日

@author: raytine
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2

问题：寻找一个列表内最长的摆动序列，摆动序列是指num[i+1]-nums[i]要与nums[i]-nums[i-1]符号相反

思路：使用动态规划法，但是我的方法效果比较差，耗时较长。
查看答案后发现一种O（n）时间复杂度就可以解决的方法。如果nums[0]<nums[1]（递增），并且nums[2]<nums[1]（递减），那么res+=1。但如果nums[2]>=nums[1]，
那么保留pre=nums[2]（这里可以这么想：之后要的是递减的状态，nums[2]>=nums[1]，可以认为nums[2]比nums[1]接下来更有形成递减状态的可能，所以保留pre=nums[2]）。
后面的数只要和pre（nms[2]）比较就可以了。
如果nums[0]>nums[1]的情况也是相似的。

0%
'''
# class Solution(object):
#     def wiggleMaxLength(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         length = len(nums)
#         save = {}
#         def getChangeWay(i, before, way):
#             if before == None:
#                 change_way = None
#             elif before > nums[i]:
#                 change_way = 'down'
#             elif before < nums[i]:
#                 change_way = 'up'
#             else:
#                 change_way = way
#             return change_way
#         
#         def getResult(i, way, num, before):
# #             print (i,way,num,before)
#             if i == length:
#                 save[(i, way, num)] = num
#                 return num
#             if (i, way, num) in save:
#                 return save[(i, way, num)]
#             change_way = getChangeWay(i, before, way)
#             if before == None:
#                 result = max(getResult(i + 1, way, num, before), getResult(i + 1, change_way, num + 1, nums[i]))
#             elif nums[i] > before:
#                 if way == 'up':
#                     result = getResult(i + 1, way, num, before)
#                 else:
#                     result = max(getResult(i + 1, way, num, before), getResult(i + 1, change_way, num + 1, nums[i]))
#             elif nums[i] < before:
#                 if way == 'down':
#                     result = getResult(i + 1, way, num, before)
#                 else:
#                     result = max(getResult(i + 1, way, num, before), getResult(i + 1, change_way, num + 1, nums[i]))
#             else:
#                 result = getResult(i + 1, way, num, before)
#             save[(i, way, num)] = num
#             return result
#         
#         return getResult(0, None, 0, None)

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # trivial case
        if (len(nums) < 2):
            return len(nums)
        # create array of diffs
        diffs = []
        for i in range(1, len(nums)):
            x = nums[i] - nums[i - 1]
            # ignore diffs of 0 as they don't count as turning points
            if (x != 0):
                diffs.append(x)
        # if there were diffs of only 0, then seq length is 1
        if (not diffs):
            return 1
            
        cnt = 1 # min seq length at this stage
        # now count the number of times the sign of diff between consecutive numbers changes
        # that will be equal to the max wiggle subseq length
        for i in range(1, len(diffs)):
            prod = diffs[i] * diffs[i - 1]
            if (prod < 0):
                cnt += 1
                
        return cnt + 1

a = Solution()
print a.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
                    