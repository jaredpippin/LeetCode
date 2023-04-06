class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['123']
        for i in s:
            if i == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
                continue
            elif i == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
                continue
            elif i == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
                continue
            else:
                stack.append(i)
            
        if len(stack) == 1:
            return True
        else:
            return False