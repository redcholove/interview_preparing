'''
Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
'''

class Solution:
    def insert(self, intervals, newInterval):
        #find pivot to insert newInterval

        #insert or merge newInterval

        #insert or merge result

        result = []
        iLen = len(intervals)
        
        if iLen == 0:
            return [newInterval]
        #判斷頭部 小的在前面
        pivot = iLen

        for i in range(iLen):
            if newInterval[0] < intervals[i][0]:
                if not result or result[-1][1] < newInterval[0]:
                    result.append(newInterval)
                else:
                    result[-1][1] = max(result[-1][1], newInterval[1])
                pivot = i
                break
            else:
                result.append(intervals[i])
        
        if pivot == iLen:
            if result[-1][1] < newInterval[0]:
                result.append(newInterval)
            else:
                result[-1][1] = max(result[-1][1], newInterval[1])
        else:
            for i in range(pivot, iLen):
                if result[-1][1] < intervals[i][0]:
                    result.append(intervals[i])
                else:
                    result[-1][1] = max(result[-1][1], intervals[i][1])

        return result



if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    result = sol.insert(intervals, newInterval)
    print(result)
