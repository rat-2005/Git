class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        while(i<len(nums)):
            if(0<nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]):
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i=i+1
        final=[]
        for i in range(0,len(nums)):
            if(i+1!=nums[i]):
                final.append(i+1)

        return(final)
        