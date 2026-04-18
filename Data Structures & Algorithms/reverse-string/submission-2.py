class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # TC: O(n)
        # SC: O(n)
        def recursion_reverse(l, r):
            if l < r:
                recursion_reverse(l+1, r-1)
                s[l], s[r] = s[r], s[l]

        recursion_reverse(0, len(s)-1)
        
        