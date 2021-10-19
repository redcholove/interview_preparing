class Solution:
    def combinationSum(self, candidates, target):
        #dfs + backtracking
        #ele 可以重複使用

        self.result = []
        cLen = len(candidates)
        
        if cLen == 0:
            return self.result
    
        candidates.sort()
        def dfs(candidates, target, start,  path):
            if target == 0:
                self.result.append(path)
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    dfs(candidates, target - candidates[i], i, path + [candidates[i]])
                else:
                    return
        
        dfs(candidates, target, 0, [])

        return self.result


if __name__ == '__main__':
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    result = sol.combinationSum(candidates, target)
    print(result)
    print('success')
    print('time complexity: O(?)')
    print('space complexity: O(?)')

