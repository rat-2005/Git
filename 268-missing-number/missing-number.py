class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)):
            if(0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]):
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i=i+1


        print(nums)
        
        for i in range(0,len(nums)):
            if i+1!=nums[i]:
                return i+1

        return 0

    

        