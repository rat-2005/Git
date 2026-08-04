class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        A=[0]*(len(nums))
        A[0]=nums[0]
        for x in range(1,len(nums)):
            A[x]=nums[x]+A[x-1]
        return A