"""
Problem Description
Given a 2D integer array A, return the transpose of A.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
A = [[1, 2],[1, 2],[1, 2]]    => Expected:  A = [[1, 2], [1, 2], [1, 2]]


"""


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers

    def solve(self, A):
        ans = []
        for c in range(0, len(A[0])):
            temp = []
            for r in range(0, len(A)):
                temp.append(A[r][c])
            ans.append(temp)
        return ans


# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = [[1, 2], [1, 2], [1, 2]]
s1 = Solution()
ans = s1.solve(A)
print(f"Answer is :{ans}")
