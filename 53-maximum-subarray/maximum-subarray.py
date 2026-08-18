class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=nums[0]
        max_sum=nums[0]
        for x in range(1,len(nums)):
            current_sum=max(current_sum+nums[x],nums[x])
            max_sum=max(max_sum,current_sum)

        return(max_sum)










        