class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for x in range(0,len(matrix)):
            for y in range(x,len(matrix[0])):
                matrix[x][y],matrix[y][x]=matrix[y][x],matrix[x][y]

        for x in matrix:
            x.reverse()

        