
class Solution:
    def reverse(self, x: int) -> int:

        dup=x
        dup=abs(dup)
        final=0
        p=0
        while(dup>0):
            rem=dup%10
            final=final*10+rem
            dup=dup//10
            p=p+1
        if final not in range(-2**(31),2**(31)):
            return 0
        if(x<0):
            return -final
        else:
            return final
        
        

        