class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        dup=[1,1]
        i=2
        while(i<rowIndex+1):
            new=[1]
            for x in range(0,i-1):
                new.append(dup[x]+dup[x+1])
            i=i+1
            new.append(1)
            dup=new
        return dup
            

            



            




        

