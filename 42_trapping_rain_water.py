class Solution:
	def getRightHeight(self, height):
		hLen = len(height)
		rightHeight = [0 for _ in range(hLen)]
		for i in range(hLen-1, -1, -1):
			if i == hLen - 1:
				rightHeight[i] = height[i]
			else:
				rightHeight[i] = max(height[i], rightHeight[i+1])
		return rightHeight
	
	def getTrapWater(self, height, rightHeight):
		result = 0
		hLen = len(height)
		leftHeight = height[0]

		for i in range(1, hLen):
			leftHeight = max(leftHeight, height[i])	
			h = min(leftHeight, rightHeight[i])
			
			if height[i] < h:
				result += (h-height[i])
		return result
			
	def trap(self, height):
		hLen = len(height)
		if hLen <= 2:
			return 0
		#record right height
		#record left height and add trap water
		
		rightHeight = self.getRightHeight(height)
		result = self.getTrapWater(height, rightHeight)
		
		return result
		

if __name__ == '__main__':
	sol = Solution()
	height = [0,1,0,2,1,0,1,3,2,1,2,1]
	result = sol.trap(height)
	print(result)
	print('success')
	print('time complexity: O(n)')
	print('space complexity: O(n)')
