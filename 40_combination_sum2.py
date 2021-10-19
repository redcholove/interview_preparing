'''
[10,1,2,7,6,1,5]
[1,1,2,5,6,7,10]
'''

class Solution:
    def combinationSum2(self, candidates, target):
        #只能用一次 ele不能重複使用
        
        self.result = []

        if len(candidates) == 0:
            return self.result
        
        candidates.sort()
        def dfs(candidates, target, path, start):
            if target == 0:
                self.result.append(path)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    return

                dfs(candidates, target-candidates[i], path + [candidates[i]], i+1)
        
        dfs(candidates, target, [], 0)

        return self.result


if __name__ == '__main__':
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = sol.combinationSum2(candidates, target)
    print(result)
    print('success')
    print('time complexity: O(?)')
    print('space complexity: O(?)')
