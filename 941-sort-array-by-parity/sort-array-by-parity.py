class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        writer=0
        for reader in range(0,len(nums)):
            if nums[reader]%2==0:
                nums[reader],nums[writer]=nums[writer],nums[reader]
                writer+=1
        return nums
        