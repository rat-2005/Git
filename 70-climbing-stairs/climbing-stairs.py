class Solution:
    total=0
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        total=0
        def inter(value):
            if(value==n):
                return 1
            elif(value>n):
                return 0
            if dp[value]!=-1:
                return dp[value]
            total=inter(value+1)+inter(value+2)
            dp[value]=total
            return total
        return inter(0)



        
       
        

        