"""
Problem Description
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.

Find the minimum cost to remove all elements from the array.


Input:   A = [2, 1]
Output:  4
Explanation :
 Given array A = [2, 1]
 Remove 2 from the array => [1]. Cost of this operation is (2 + 1) = 3.
 Remove 1 from the array => []. Cost of this operation is (1) = 1.
 So, total cost is = 3 + 1 = 4.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)
        total=0
        for i in range(len(A)):
            total+=(A[i]*(i+1))
        return total


s1 = Solution()
A = [1,2,3]
result = s1.solve(A)
print(f"The minimum cost for Array A: {A} is >>>>> {result}")


