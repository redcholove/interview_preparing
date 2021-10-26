class Solution:
    def doOperator(self, pre, preOp, cur):
        if preOp == '+':
            pre.append(int(cur))
        elif preOp == '-':
            pre.append(int(cur) * -1)
        elif preOp == '*':
            first = pre.pop()
            pre.append(first*int(cur))
        else:
            first = pre.pop()
            pre.append(int(first/int(cur)))

    def calculate(self, s: str) -> int:
        #正確格式
        sLen = len(s)
        
        if sLen == 1:
            return int(s)
        
        operators = {'+', '-', '*', '/'}
        
        pre = []
        preOp = '+'
        result = 0
        
        tmp = ''
        for i in range(sLen):
            if s[i] in operators:
                self.doOperator(pre, preOp, tmp)
                preOp = s[i]
                tmp = ''
            elif s[i] != ' ':
                tmp += s[i]
                
        self.doOperator(pre, preOp, tmp)
        
        for p in pre:
            result += p
            
        return result
