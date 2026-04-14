class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # TC: O(n*logm)
        l = 1
        r = max(piles)
        res = r         # SC: O(1)
        while l <= r:
            m = (l+r)//2
            time = 0
            for i in piles:
                time += math.ceil(i/m)
            if time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

        # n = length of input array piles
        # m = max no. of bananas in pile