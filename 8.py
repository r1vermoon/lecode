'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup=set()
        left=0
        n=len(s)
        max_len=0
        cur_len=0
        for i in range(n):
            cur_len+=1
            while s[i] in lookup:
                lookup.remove(s[left])
                left+=1
                cur_len-=1
            lookup.add(s[i])
            if cur_len>max_len:
                max_len=cur_len
        return max_len