class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged=[intervals[0]]
        for x in intervals[1:]:
            if merged[-1][1]>=x[0]:
                merged[-1][1]=max(x[1],merged[-1][1])
            else:
                merged.append(x)
        return merged


            



        