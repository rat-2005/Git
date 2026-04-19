class Solution:
    def rob(self, nums: List[int]) -> int:
        rob=[0]*len(nums)
        if(len(nums)==1):
            rob[0]=nums[0]
        elif (len(nums)>=2):
            rob[0]=nums[0]
            rob[1]=nums[1]
        for x in range(2,len(nums)):
            value=max(rob[0:x-1])
            rob[x]=nums[x]+value

        return max(rob)

        