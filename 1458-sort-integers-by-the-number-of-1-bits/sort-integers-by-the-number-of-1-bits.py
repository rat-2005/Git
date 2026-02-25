class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        map=[]
        for x in arr:
            map.append(self.decimal_to_binary(x))
        self.sort(map)
        return([x[1] for x in map])



    def decimal_to_binary(self,a):
        dup=a
        x=1
        final=0
        no_of_one=0
        while(dup!=0):
            rem=dup%2
            if(rem==1):
                no_of_one=no_of_one+1
            dup=dup//2
            final=final+rem*x
            x=x*10
        return[no_of_one,a]

    
    def sort(self,map):
        for x in range(0,len(map)):
            for y in range(0,len(map)-1):
                if(map[y][0]>map[y+1][0]):
                    map[y+1],map[y]=map[y],map[y+1]
                if(map[y][0]==map[y+1][0]):
                    if(map[y][1]>map[y+1][1]):
                        map[y+1],map[y]=map[y],map[y+1]
    


        