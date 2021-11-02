'''
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
'''
import collections

#給四個array,length 相同 並且都大於1
#return 有多少 tuple(四個array的idx) -> 加起來 = 0

#for loop nums1, nums2 -> combine a val
#record nums1 + nums2 val -> frequency
#for loop nums3, nums4 -> combine a val -> find frequency -> add for result
#做two sum
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        frequency = collections.Counter()
        
        result = 0
        
        for n1 in nums1:
            for n2 in nums2:
                frequency[n1+n2] += 1
                
        for n3 in nums3:
            for n4 in nums4:
                target = 0 - n3 - n4
                result += frequency[target]
                
        return result
        
if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    result = sol.fourSumCount(nums1, nums2, nums3, nums4)
    print(result)
