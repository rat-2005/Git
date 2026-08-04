class NumArray:

    def __init__(self, nums: List[int]):
        self.A=[0]*len(nums)
        self.A[0]=nums[0]
        for x in range(1,len(nums)):
            self.A[x]=self.A[x-1]+nums[x]
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.A[right]
        return (self.A[right]-self.A[left-1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)