'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        pos1=0
        pos2=len(matrix)-1
        while pos1<pos2:
            add=0
            while add<pos2-pos1:
                temp=matrix[pos2-add][pos1]
                matrix[pos2-add][pos1]=matrix[pos2][pos2-add]
                matrix[pos2][pos2-add]=matrix[pos1+add][pos2]
                matrix[pos1+add][pos2]=matrix[pos1][pos1+add]
                matrix[pos1][pos1+add]=temp
                add=add+1
            pos1=pos1+1
            pos2=pos2-1