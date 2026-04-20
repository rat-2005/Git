import math
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        nums = []
        i = 1
        while i**x <= n:
            nums.append(i)
            i += 1

        memo={}
        def functio(value,index):
            
            if (n==value):
                return 1
            elif(n<value):
                return 0
            if index>=len(nums):
                return 0
            if((value,index) in memo):
                return memo[(value,index)]
            include=functio(value+(nums[index])**x,index+1)
            exclude=functio(value,index+1)
            memo[(value,index)]=include+exclude%(10**9+7)
            return (include+exclude)%(10**9+7)
        return functio(0,0)
        
            



        
        