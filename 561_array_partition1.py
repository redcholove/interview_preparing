class Solution:
    def arrayPairSum(self, nums):
        resultList = sorted(nums)
        ans = 0
        for i in range(len(nums)):
            # 雙數idx的val
            if i % 2 == 0:
                ans += resultList[i]

        return ans

if __name__ == '__main__':
    sol = Solution()
    nums = [6,2,6,5,1,2]
    result = sol.arrayPairSum(nums)
    print(result)
    print('success')
    print('time complexity: O(nlogn)')
    print('space complexity: O(1)')
