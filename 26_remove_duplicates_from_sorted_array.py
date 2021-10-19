'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

[0,0,1,1,1,2,2,3,3,4]
           i
                     l
[0,1,2,3,4]

[0,0]
   i
      l
'''
class Solution:
    def removeDuplicates(self, nums):
        #two pointer
        #first -> 存下來的 idx
        #sec -> 替換的idx
        nLen = len(nums)
        if nLen <= 1:
            return nLen
        l = 0
        r = 0

        while r < nLen:
            if r == 0:
                l += 1
                r += 1
            else:
                if nums[r] == nums[r-1]:
                    r += 1
                else:
                    nums[l] = nums[r]
                    r += 1
                    l += 1
        return l


if __name__ == '__main__':
    sol = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = sol.removeDuplicates(nums)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
