# https://leetcode.com/contest/weekly-contest-384/problems/modify-the-matrix/
# Given a 0-indexed m x n integer matrix matrix,
# create a new 0-indexed matrix called answer.
# Make answer equal to matrix,
# then replace each element with the value -1 with the maximum element in its respective column.

# matrix[i][j] = max(matrix[k][j] for k in range(n))

from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = max(matrix[k][j] for k in range(n))
        return matrix


s = Solution()
assert s.modifiedMatrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]]) == [[1, 2, 9], [4, 8, 6], [7, 8, 9]]
assert s.modifiedMatrix([[3, -1], [5, 2]]) == [[3, 2], [5, 2]]
assert s.modifiedMatrix([[1, 2, -1, -1, 9], [4, -1, 6, 4, -1], [7, 8, 9, 5, 5]]) == [[1, 2, 9, 5, 9], [4, 8, 6, 4, 9], [7, 8, 9, 5, 5]]

