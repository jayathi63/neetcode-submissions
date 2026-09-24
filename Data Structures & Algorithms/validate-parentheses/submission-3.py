class Solution:
    def isValid(self, s: str) -> bool:

        maps = {'}':'{', ']':'[', ')':'('}
        stack = []

        for i in s:
            if i in {'(','{','['}:
                stack.append(i)
            else:
                k = stack.pop() if stack else None
                v = maps[i]
                
                if v != k:
                    return False
        return True if not stack else False
                    
