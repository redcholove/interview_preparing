'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

'''
class Solution:
    def countAndSay(self, n):
        if n == 1: return '1'

        dp = ['0' for _ in range(n+1)]
        dp[1] = '1'

        for i in range(2, len(dp)):
            #判斷連續幾個數字相同
            tmp = ''
            prev = dp[i-1][0]
            count = 1
            for j in range(1, len(dp[i-1])):
                if dp[i-1][j] == prev:
                    count += 1
                else:
                    tmp += str(count)
                    tmp += str(prev)
                    prev = dp[i-1][j]
                    count = 1
            tmp += str(count)
            tmp += str(prev)
            dp[i] = tmp

        return dp[-1]

if __name__ == '__main__':
    sol = Solution()
    n = 4
    result = sol.countAndSay(n)
    print(result)
    print('success')
    print('time complexity: O(n^2)')
    print('space complexity: O(n)')
