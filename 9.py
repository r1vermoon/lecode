'''
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
'''
class Solution(object):
    def findAnagrams(self, s, p):
        n,m,res=len(s),len(p),[]
        p_cnt=[0]*26
        s_cnt=[0]*26
        if n<m: return res
        for i in range(m):
            p_cnt[ord(p[i])-ord('a')]+=1
            s_cnt[ord(s[i])-ord('a')]+=1
        if p_cnt==s_cnt:
            res.append(0)
        
        for i in range(m,n):
            s_cnt[ord(s[i-m])-ord('a')]-=1
            s_cnt[ord(s[i])-ord('a')]+=1
            if p_cnt==s_cnt:
                res.append(i-m+1)
        return res