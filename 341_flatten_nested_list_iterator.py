# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

#給一個list裡面每個元素有可能是list也有可能是element, 攤平他 然後提供next 和 hasNext的功能
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flattenHelper(nl):
            tmp = []
            
            for n in nl:
                if n.isInteger():
                    tmp.append(n.getInteger())
                else:
                    tmp.extend(flattenHelper(n.getList()))
            return tmp
        self.flatten = deque(flattenHelper(nestedList))
        
    def next(self) -> int:
        return self.flatten.popleft()
    
    def hasNext(self) -> bool:
         return self.flatten

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
