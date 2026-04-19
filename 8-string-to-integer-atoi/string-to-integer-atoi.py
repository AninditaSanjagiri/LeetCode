class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Read digits
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1

        result *= sign

        # Clamp range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
        