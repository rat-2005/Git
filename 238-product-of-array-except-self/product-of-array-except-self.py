class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # array=[x for x in nums]
        # for x in range(0,len(nums)):
        #     t=1
        #     for f in nums[:x]+nums[x+1:]:
        #         t=t*f
        #     array[x]=t
        # return array
        left_prod=1
        left_array=[1 for x in range(0,len(nums))]
        for x in range(0,len(nums)):
            left_array[x]=left_prod
            left_prod*=nums[x]

        print(left_array)

        right_prod=1
        right_array=[1 for x in range(0,len(nums))]
        for x in range(0,len(nums))[::-1]:
            right_array[x]=right_prod
            right_prod*=nums[x]

        final=[1 for x in range(0,len(nums))]
        for x in range(0,len(nums)):
            final[x]=right_array[x]*left_array[x]
        return(final)

        



        