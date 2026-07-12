class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        max_value=0
        for i,c in enumerate(s):
            if c=="(":
                stack.append(i)
            else:
                stack.pop()
                if stack==[]:
                    stack.append(i)
                else:
                    value=i-stack[-1]
                    max_value=max(max_value,value)

        return max_value

