class Solution(object):
    def isValid(self, s):
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}
    
        for char in s:
         if char in ('(', '[', '{'):
            stack.append(char)  # push to stack
         else:
             if len(stack) == 0 or stack[-1] != matching[char]:
                 return False
             stack.pop()  # pop from stack
    
        return len(stack) == 0  # what does empty stack mean?
        