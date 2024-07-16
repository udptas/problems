# Count Increasing Triplets
# Problem Description
# You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]
# Input 1: A = [1, 2, 4, 3]  Output: 2
#           Here The triplets that satisfy the conditions are [1, 2, 3] and [1, 2, 4].
# Input 2: A = [2, 1, 2, 3]  Output: 1

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Expansion method, Here taking the mid value and checking the nos that are less in left and nis that are
        # greater in right.
        res = 0
        for j in range(1, len(A) - 1):
            l, m= 0, 0
            # print(A[j])
            for i in range(j - 1, -1, -1):  # left Side smaller values
                if A[i] < A[j]:
                    l += 1

            for k in range(j + 1, len(A)):  # right side greater values
                if A[j] < A[k]:
                    m += 1
            # print(l,m)
            res += l * m
        return res


s = Solution()
A = [1, 2, 4, 3]
B = [26,23,23,16,27,18,7]
print(f"For the list {A}, the count of such numbers are: {s.solve(A)}")
print(f"For the list {B}, the count of such numbers are: {s.solve(B)}")
