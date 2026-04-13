class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for l in range(len(matrix)):
        #     for r in range(len(matrix[0])):
        #         if matrix[l][r] == target:
        #             return True
        # return False

        # TC: O(m*n)
        # SC: O(1)
        l = 0
        r = len(matrix[0]) - 1
        for i in range(len(matrix)):
            if matrix[i][l] <= target and matrix[i][r] >= target:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
        return False