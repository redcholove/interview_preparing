class Solution:
    def nextPermutation(self, nums):
        nLen = len(nums)
        pivot = nLen + 1
        
        for i in range(nLen-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i-1
                break
        if pivot == nLen + 1:
            nums.reverse()
            return
        
        swap = nLen - 1
        
        while nums[pivot] >= nums[swap]:
            swap -= 1
        
        nums[pivot], nums[swap] = nums[swap], nums[pivot]

        l = pivot + 1
        r = nLen - 1
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        return



if __name__ == '__main__':
    sol = Solution()
    nums = [1,1,5]
    sol.nextPermutation(nums)
    print(nums)
    print('success')
    print('time complexity: O(n)')
    print('space complexity: O(1)')
