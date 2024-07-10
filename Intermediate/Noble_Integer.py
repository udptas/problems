"""
Noble Integer:
Problem Description
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.

Input Format
First and only argument is an integer array A.

Output Format
Return 1 if any such integer p is present else, return -1.

Input 1:
 A = [3, 2, 1, 3]
Output:
 For integer 2, there are 2 greater elements in the array...

"""


class Solution:
    def __init__(self):
        pass

    def solve(self,A):
        A.sort(reverse=True)
        greater=-1
        pval = float('INF')  # Initializing with INFnity, incase of smaller element
                             # we could have initialized it with a -INF
        # print(A)
        for i in range(len(A)):
            val = A[i]
            if val != pval:
                greater = i
            if val == greater:
                # print(greater)
                return 1
            pval = val
        return -1


s1 = Solution()
A = [3, 2, 1, 3]
ans = s1.solve(A)
print(f"Answer is {ans}")
