class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        final=[]
        for x in range(0,len(nums)):
            if x>0 and nums[x]==nums[x-1]:
                continue
            for y in range(x+1,len(nums)):
                if y>x+1 and nums[y]==nums[y-1]:
                    continue
                pivot=y
                pointer1=y+1
                pointer2=len(nums)-1
                while(pointer1<pointer2):
                    value=nums[x]+nums[pivot]+nums[pointer1]+nums[pointer2]
                    if value<target:
                        pointer1+=1
                    elif target<value:
                        pointer2-=1
                    else:
                        final.append([nums[x],nums[pivot],nums[pointer1],nums[pointer2]])
                        pointer1+=1
                        pointer2-=1

                        while(pointer1<pointer2 and nums[pointer1]==nums[pointer1-1]):
                            pointer1+=1    
                        while(pointer1<pointer2 and nums[pointer2]==nums[pointer2+1]):
                            pointer2-=1                    

        return final


                


        