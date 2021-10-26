class Solution:
    def traversalCand(self, gas, cost, i):
        remain = gas[i] - cost[i]
        
        curPosition = i + 1 if i != len(gas) - 1 else 0
        while curPosition != i:
            remain += (gas[curPosition] - cost[curPosition])
            if remain < 0:
                return False
            if curPosition == len(gas) - 1:
                curPosition = 0
            else:
                curPosition += 1
        return True 
        
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #找出一個起始點, 可以繞一整圈
        
        #greedy
        
        #gas[i] >= cost[i] -> candidate of starting index
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                if self.traversalCand(gas, cost, i):
                    return i
        return -1
        #traversal for checking assumation
        
        
