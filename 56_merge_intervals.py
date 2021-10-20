'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

class Solution:
    def merge(self, intervals):
        result = []
        if not intervals:
            return result

        #sort
        #for loop 判斷 後面的頭 <= 前面的尾巴的話 merge 不然append 
        
        intervals.sort()
        iLen = len(intervals)
        for i in range(iLen):
            if not result or result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(intervals[i][1], result[-1][1])
        return result
    
if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = sol.merge(intervals)
    print(result)
    print('success')
    print('time complexity: O(nlogn)')
    print('space complexty: O(n)')
