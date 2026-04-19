class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      a=cost[0]
      b=cost[1]
      for x in range(2,len(cost)):
        tem=cost[x]+min(a,b)
        a=b
        b=tem
      return min(a,b)
    

        