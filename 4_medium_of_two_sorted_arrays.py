class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        aLen = len(nums1)
        bLen = len(nums2)
        isOdd = (aLen + bLen) % 2 == 1
        mid = int((aLen + bLen) / 2)
        first = None
        sec = None
        idx1 = 0
        idx2 = 0

        while (idx1 < aLen or idx2 < bLen) and (idx1 + idx2 <= mid):
            val = 0

            if idx1 >= aLen:
                #operator nums2
                val = nums2[idx2]
                idx2 += 1
            elif idx2 >= bLen:
                #operator nums1
                val = nums1[idx1]
                idx1 += 1
            else:
                if nums1[idx1] < nums2[idx2]:
                    val = nums1[idx1]
                    idx1 += 1
                else:
                    val = nums2[idx2]
                    idx2 += 1

            if first == None:
                first = val
            elif sec == None:
                sec = val
            else:
                first = sec
                sec = val

        if isOdd:
            return sec if sec else first
        else:
            return (sec + first)/2


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,3]
    nums2 = [2]
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(result)
    print('success')
    print('time complexity: O((m+n) /2)')
    print('space complexity: O(1)')
