class Sort:
    def selectionSort(self, arr):
        result = list(arr)
        rLen = len(result)

        for i in range(rLen):
            tmp = i
            for j in range(i+1, rLen):
                if result[j] < result[tmp]:
                    tmp = j
            result[i], result[tmp] = result[tmp], result[i]
        return result

    def insertionSort(self, arr):
        result = list(arr)
        rLen = len(result)

        for i in range(1, rLen):
            cur = result[i]
            j = i - 1

            while j >= 0 and result[j] > cur:
                result[j+1] = result[j]
                j -= 1
            result[j+1] = cur
        return result


    def bubbleSort(self, arr):
        result = list(arr)
        rLen = len(result)

        for i in range(rLen):
            flag = True
            for j in range(rLen-i-1):
                if result[j] > result[j+1]:
                    flag = False
                    result[j], result[j+1] = result[j+1], result[j]
            if flag:
                return result
        return result
    
    def mergeHelper(self, arr1, arr2):
        result = []
        aLen = len(arr1)
        bLen = len(arr2)
        i = 0
        j = 0

        while i < aLen or j < bLen:
            if i >= aLen:
                result.append(arr2[j])
                j += 1
            elif j >= bLen:
                result.append(arr1[i])
                i += 1
            else:
                if arr1[i] < arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1
        return result

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr

        l = 0
        r = len(arr)
        mid = int(l + (r-l) / 2)

        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.mergeHelper(left, right)

if __name__ == '__main__':
    solution = Sort()
    arr = [37,17,85,21,65,95,80,56,3,68]
    print('origin arr: ' + str(arr))
    print()
    selection = solution.selectionSort(arr)
    print('selection sort: ' + str(selection))
    print('all time complexity: O(n^2)')
    print('space complexity: O(1)')
    print()

    insertion = solution.insertionSort(arr)
    print('insertion sort: ' + str(insertion))
    print('best time complexity: O(n), worst time complexity: O(n^2), average time complexity: O(n^2)')
    print('space complexity: O(1)')
    print()

    bubble = solution.bubbleSort(arr)
    print('bubble sort: ' + str(bubble))
    print('best time complexity: O(n), worst time complexity: O(n^2), average time complexity: O(n^2)')
    print('space complexity: O(1)')
    print()

    merge = solution.mergeSort(arr)
    print('merge sort: ' + str(merge))
    print('all time complexity: O(nlogn)')
    print('space complexity: O(n)')
    print()


