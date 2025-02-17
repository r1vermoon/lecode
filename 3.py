'''
最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxlen=0
        nums=set(nums)
        for i in nums:
            if i-1 not in nums:
                count=1
                while i+1 in nums:
                    count=count+1
                    i=i+1
                if maxlen<count:
                    maxlen=count
        return maxlen
