class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for l in range(len(matrix)):
            for r in range(len(matrix[0])):
                if matrix[l][r] == target:
                    return True
        return False