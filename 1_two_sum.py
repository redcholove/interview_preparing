class Solution:
    def twoSum(self, nums, target):
        appears = dict()
        nLen = len(nums)

        for i in range(nLen):
            cand = target - nums[i]

            if cand in appears:
                return [i, appears[cand]]
            else:
                appears[nums[i]] = i
        
        return [-1,-1]

if __name__ == '__main__':
    sol = Solution()

    nums = [2,7,11,15]
    target = 9
    result = sol.twoSum(nums, target)
    print(result)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(n)')
