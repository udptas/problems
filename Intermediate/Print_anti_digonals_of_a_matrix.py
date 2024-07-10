""" Anti Diagonals
Problem Description:
    Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.
    Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
    The vacant spaces in the grid should be assigned to 0.

Input 1:
    1 2 3
    4 5 6
    7 8 9

Output 1:
    1 0 0
    2 4 0
    3 5 7
    6 8 0
    9 0 0
"""



class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):

        ans = []
        # The Ans we are deviding in two phases, first phase we are starting from column from 0 to column n-1
        # and then decrementing the column from each by one and while raw strarts from 0 and gets incremented
        #       00  01  02  03          Column 0 Raw 0 => Column 1 Row 0. => Column 0 Row 1 => Column 2 Row 0
        #       10  11  12  /13          => Column 1 Row 1 => Column 0 Row 2 => Column 3 Row 0 => Column 2 Row 1
        #       20  21  /22  23         => Column 1 Row 2 => Column 0 Row 3   => Column 4 Row 0 XXX The loop
        #       30  /31  32  33         => will end here.  Now we need to cover 13 => 22=> 31 => 23 => 32 => 33
        for i in range(0, len(A[0])):
            r, c = 0, i
            temp, j = [0] * (len(A)), 0
            # print(temp)
            while (r < len(A) and c >= 0):
                # print(r,c)
                # print(A[r][c])
                temp[j] = A[r][c]
                r += 1
                c -= 1
                j += 1
            # print(temp)
            ans.append(temp)
        # Now we will be iterating the columns which starts at 1 to 3, that were not covered in the last loop
        for i in range(1, len(A)):
            r, c = i, len(A) - 1
            temp, j = [0] * (len(A)), 0
            while (r < len(A) and c >= 0):
                # print(r,c)
                # print(A[r][c])
                temp[j] = A[r][c]
                r += 1
                c -= 1
                j += 1
            # print(temp)
            ans.append(temp)
            # print(ans)
        return ans


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s1=Solution()
ans = s1.diagonal(A)
print(f"The Expected answer is {ans}")