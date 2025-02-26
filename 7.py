'''
接雨水
给定 n 个非负整数表示每个宽度为
 1 的柱子的高度图，
 计算按此排列的柱子，
 下雨之后能接多少雨水。'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        leftheight=[0]*len(height)
        rightheight=[0]*len(height)
        leftheight[0]=height[0]
        for i in range(1,len(height)):
            leftheight[i]=max(leftheight[i-1],height[i])
        rightheight[-1]=height[-1]
        for i in range(len(height)-2,-1,-1):
            rightheight[i]=max(rightheight[i+1],height[i])
        
        res=0
        for i in range(0,len(height)):
            summ = min(rightheight[i],leftheight[i])-height[i]
            res += summ

        return res