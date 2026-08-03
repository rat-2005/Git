class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        final=[]
        r=0
        c=0
        ROW=len(mat)-1
        COL=len(mat[0])-1
        while(r<=ROW and c<=COL):
            if(r+c)%2==0:
                if (c==COL):
                    final.append(mat[r][c])
                    r+=1               
                elif(r==0):
                    final.append(mat[r][c])
                    c+=1
                else:
                    final.append(mat[r][c])
                    c+=1
                    r-=1
            elif(r+c)%2!=0:
                if(r==ROW):
                    final.append(mat[r][c])
                    c+=1               
                elif(c==0):
                    final.append(mat[r][c])
                    r+=1
                else:
                    final.append(mat[r][c])
                    r+=1
                    c-=1

        return(final)

                


        