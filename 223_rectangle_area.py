class Solution:
    def mergeInterval(self, xInterval, yInterval):
        xInterval.sort()
        yInterval.sort()
        if xInterval[1][0] > xInterval[0][1] or yInterval[1][0] > yInterval[0][1]:
            return 0
        
        x = min(xInterval[0][1], xInterval[1][1]) - max(xInterval[0][0], xInterval[1][0])
        y = min(yInterval[0][1], yInterval[1][1]) - max(yInterval[0][0], yInterval[1][0])
        return  x * y
        
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:        
        x1 = [ax1, ax2]
        y1 = [ay1, ay2]
        
        x2 = [bx1, bx2]
        y2 = [by1, by2]
        
        val = ((ax2-ax1) * (ay2-ay1))
        val += ((bx2-bx1) * (by2-by1)) 
        val -= self.mergeInterval([x1, x2], [y1, y2])
        
        return val
