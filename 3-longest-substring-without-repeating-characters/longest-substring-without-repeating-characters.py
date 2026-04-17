class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=0
        longest=0

        for right in range(len(s)):
            char=s[right]

            if char in seen:
                left=max(left,seen[char]+1)

            seen[char]=right
            longest=max(longest,right-left+1)
        return longest

        