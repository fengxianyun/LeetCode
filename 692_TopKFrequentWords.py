# coding: utf-8
'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
    
给出一列表单词（非空），先按照频率排序，再按字母表顺序排序，最后输出给定个数的单词
22.20%
'''

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        save = {}
        for i in  words:
            if i not in save:
                save[i] = 0
            save[i] += 1
        item_tuple = save.items()
        save = sorted(item_tuple, key = lambda x:(-x[1], x[0]))
        result = []
        for i in range(k):
            result.append(save[i][0])
        return result
        
