'''
盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        area=0
        while(right>left):
            cur=min(height[left],height[right])*(right-left)
            area=max(cur,area)
            if (height[right]>height[left]):
                left+=1
            else:
                right-=1
        return area