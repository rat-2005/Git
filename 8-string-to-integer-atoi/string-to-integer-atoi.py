class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        s=s.strip()
        i=0
        n=""
        si=""

        if not s:
            return 0
        if "+" in s[0]:
            s=s[1:]
            si="+"

        elif "-" in s[0]:
            s=s[1:]
            si="-"

        while(i<len(s)):
            if s[i].isnumeric():
                i=i+1
            else:
                break
        if(s[0:i].isnumeric()):
            if int(si+s[0:i]) < INT_MIN:
                return INT_MIN
            if int(si+s[0:i]) > INT_MAX:
                return INT_MAX
            return (int(si+s[0:i]))

        return 0

        