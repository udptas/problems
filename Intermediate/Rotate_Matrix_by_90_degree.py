"""Problem Description
You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note: If you end up using an additional array, you will only receive partial score.

[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

"""


class Solution:
    # @param A : list of list of integers
    def __init__(self):
        pass

    def solve(self, A):
        # Getting the Transpose of the Array
        print(A)
        for i in range(0, len(A) - 1):
            for j in range(i + 1, len(A)):
                print(i, j)
                temp=A[i][j]
                A[i][j]=A[j][i]
                A[j][i]=temp
        print(f"Printing the matrix after getting the transpose is {A}")
        # Reversing the elements of each Raw
        for raw in A:
            for i in range(0, int(len(raw)//2)):
                temp=raw[i]
                raw[i]=raw[len(A)-1-i]
                raw[len(A)-1-i]=temp
        return A


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s1 = Solution()
ans = s1.solve(A)
print(f"Required answer is {A}")
