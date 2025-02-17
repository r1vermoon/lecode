'''
字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
'''
class Solution():
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        l1=[]
        d1={}

        for i in strs:
            nlist=list(i)
            plist=sorted(nlist)
            newstr=''.join(plist)
            if newstr not in d1:
                d1[newstr]=[i]
            else:
                d1[newstr].append(i)
        for i in d1:
            l1.append(d1[i])
        return l1