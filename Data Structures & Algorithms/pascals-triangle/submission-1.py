class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # TC: O(n**2)
        # SC: o(n**2)
        res = []
        for i in range(numRows):
            curr = [1] * (i+1)
            for j in range(1, i):
                curr[j] = res[i-1][j-1] + res[i-1][j]
            res.append(curr)
        return res