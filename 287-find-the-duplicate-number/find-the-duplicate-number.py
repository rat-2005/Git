class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)):
            if(0<nums[i]<=len(nums)and nums[nums[i]-1]!=nums[i]):
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i=i+1
            
        for x in range(0,len(nums)):
            if x+1!=nums[x]:
                return nums[x]

        