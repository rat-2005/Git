class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        # num=0
        # for x in range(0,len(rectangles)):
        #     for y in range(x+1,len(rectangles)):
        #         if rectangles[x][0]/rectangles[x][1]==rectangles[y][0]/rectangles[y][1]:
        #             num=num+1
        # return num

        for x in range(0,len(rectangles)):
            rectangles[x]=rectangles[x][0]/rectangles[x][1]

        hash={

        }
        for x in rectangles:
            if x not in hash:
                hash[x]=1
            else:
                hash[x]+=1

        su=0
        for x in hash:
            su=su+(hash[x]-1)*(hash[x])//2
        return su


        

        