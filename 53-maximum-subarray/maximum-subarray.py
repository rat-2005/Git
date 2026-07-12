class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=nums[0]
        max_sum=nums[0]
        for x in nums[1:]:
            current_sum=max(x,current_sum+x)
            max_sum=max(current_sum,max_sum)

        return max_sum







        