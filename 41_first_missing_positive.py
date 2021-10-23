class Solution:
	def firstMissingPositive(self, nums):
		maxPositive = len(nums)
		nums = set(nums)
		for i in range(1, maxPositive+1):
			if i not in nums:
				return i
		return maxPositive + 1
	
	def firstMissingPositive(self, nums):
		maxPositive = len(nums)
        
		for i in range(maxPositive):
		    while nums[i] > 0 and nums[i] <= maxPositive and nums[i] != nums[nums[i]-1]:
			#這邊有點特殊 要稍微注意一下
			val = nums[i]
			targetIdx = val - 1
			nums[i] = nums[nums[i]-1]
			nums[targetIdx] = val

		for i in range(len(nums)):
		    if nums[i] != i + 1:
			return i + 1
		return maxPositive + 1


if __name__ == '__main__':
	sol = Solution()
	nums = [7,8,9,11,12]
	result = sol.firstMissingPositive(nums)
	print(result)
	print('success')
	print('time complexity: O(n)')
	print('space complexity: O(n)')
