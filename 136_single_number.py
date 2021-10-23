class Solution:
    def missingNumber(self, nums):
        #solution 1 -> 梯形公式
        
        #solution 2 -> xor
        #explaintion -> xor (1 & 0) -> 1 (0 & 0, 1 & 1) -> 0
        #所以相同的數字xor之後會變0000, 剩下唯一的單獨數字跟0000 xor 會是他自己
        result = 0
        for n in nums:
            result ^= n
        return result
        
if __name__ == '__main__':
    sol = Solution()
    nums = [9,9,1,2,2]
    result = sol.missingNumber(nums)
    print(result)
    print('time complexity: O(n)')
    print('space complexity: O(1)')
