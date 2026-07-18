class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # final=[]
        # for x in range(0,len(nums)):
        #     for y in range(x+1,len(nums)):
        #         for z in range(y+1,len(nums)):
        #             if nums[x]+nums[y]+nums[z]==0:
        #                 local=[nums[x],nums[y],nums[z]]
        #                 final.append(local)
        # for x in final:
        #     x.sort()
        # o=[]
        # for x in final:
        #     if x not in o:
        #         o.append(x)

        # return o
        final=[]
        nums.sort()
        for i in range(len(nums)):
   
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            anchor=i
            left_pointer=i+1
            right_pointer=len(nums)-1
            while left_pointer<right_pointer:
                test=nums[anchor]+nums[left_pointer]+nums[right_pointer]
                if test>0:
                    right_pointer=right_pointer-1
                elif test<0:
                    left_pointer=left_pointer+1
                else:
                    final.append([nums[anchor],nums[left_pointer],nums[right_pointer]])

                    left_pointer=left_pointer+1
                    right_pointer=right_pointer-1

                    while(left_pointer<right_pointer and nums[left_pointer]==nums[left_pointer-1]):
                        left_pointer=left_pointer+1

                    while(left_pointer<right_pointer and nums[right_pointer]==nums[right_pointer+1]):
                        right_pointer=right_pointer-1
        return final



            

        