class Solution:
    def isValid(self, s: str) -> bool:
        has={"(":")","[":"]","{":"}"}
        stack=[]
        output=True
        for i in s:
            if (i in has):
                stack.append(has[i])
                output=False
            else:
                if not stack or stack.pop()!=i:
                    return False
        return not stack
        