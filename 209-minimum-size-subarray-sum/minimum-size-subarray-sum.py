class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        summ=0
        min_s=float('inf')
        for right in range(0,len(nums)):
            summ=summ+nums[right]
            while summ>=target:
                min_s=min(min_s,right-left+1)
                summ=summ-nums[left]
                left+=1
        return min_s if min_s!=float('inf') else 0


        