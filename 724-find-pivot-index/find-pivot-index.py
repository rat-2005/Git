class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        r=[0]*len(nums)
        l=[0]*len(nums)
        r[0]=nums[0]
        l[len(nums)-1]=nums[len(nums)-1]
        for x in range(1,len(nums)):
            r[x]=r[x-1]+nums[x]
        for x in range(0,len(nums)-1)[::-1]:
            l[x]=l[x+1]+nums[x]
        print(r)
        print(l)
        for x in range(0,len(nums)):
            if l[x]==r[x]:
                return x
        return -1


        
        