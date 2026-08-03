class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        final=[]
        top=0
        left=0
        bottom=len(matrix)-1
        right=len(matrix[0])-1
        while(top<=bottom and left<=right):
            for x in range(left,right+1):
                final.append(matrix[top][x])
            top+=1
            for x in range(top,bottom+1):
                final.append(matrix[x][right])
            right-=1
            if bottom>=top:
                for x in range(left,right+1)[::-1]:
                    final.append(matrix[bottom][x])
                bottom-=1
            if left<=right:
                for x in range(top,bottom+1)[::-1]:
                    final.append(matrix[x][left])
                left+=1
        return(final)
            


            


        