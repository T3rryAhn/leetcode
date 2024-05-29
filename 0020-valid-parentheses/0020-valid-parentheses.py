class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            c = s[i]
            if c in ['(', '{', '[']:
                stack.append(c)
            elif stack:
                top = stack[-1]
                if c == ')' and top == '(':
                    stack.pop()
                elif c == '}' and top == '{':
                    stack.pop()
                elif c == ']' and top == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        return True
