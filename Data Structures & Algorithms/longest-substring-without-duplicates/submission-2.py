class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        max_length = 0
        for r in range(len(s)):
            # curr_window = 0
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            curr_window = (r-l) + 1
            max_length = max(max_length, curr_window)
        return max_length