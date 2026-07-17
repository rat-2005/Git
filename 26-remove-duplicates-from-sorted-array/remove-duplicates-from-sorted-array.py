class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        insert_index=1
        for x in range(1,len(nums)):
            if nums[x]!=nums[x-1]:
                nums[insert_index]=nums[x]
                insert_index+=1
        return insert_index


            
        