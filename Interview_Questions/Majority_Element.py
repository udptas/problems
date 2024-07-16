# Majority Element
# Problem Description::
#   Given an array of size N, find the majority element. The majority element is
#   the element that appears more than floor(n/2) times. You may assume that the array is non-empty and the majority
#   element always exists in the array.
# Input: Only argument is an integer array.
# Output: Return an integer. (In case of no such element, return -1)
# Example: [2, 1, 2]  ==> Here 2 is the majority Element
# Example: [1,4,2,3,1,4,1,4,1,9,1,1,0,4,1,1,1]   ==>  Here 1 is the majority element
# Example: [1,2,3,2]  ==> Here count of 2 is 2, which is not grater than count os array element(4)/2=2, so return -1


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        f, m = 0, -1
        for i in range(len(A)):
            if f == 0:
                m = A[i]
                f = 1
            elif m == A[i]:
                f += 1
            else:
                f -= 1
            # print(f"Value of m and f are :{m, f}")
        # print(f"m is {m}")
        count = 0
        for i in range(len(A)):
            if A[i] == m:
                count += 1
        # print(f"Count of {m} in A is: {count} and length of Array is {len(A)}")
        if count > int(len(A) / 2):
            return m
        return -1


s1 = Solution()
A = [1, 4, 2, 3, 1, 4, 1, 4, 1, 9, 1, 1, 0, 4, 1, 1, 1]
B = [1, 2, 3, 2]
res1 = s1.majorityElement(A)
print(f"For input Array {A} majority element is {res1} (in case of no majority we are returning -1)")
res2 = s1.majorityElement(B)
print(f"For input Array {B} majority element is {res2} (in case of no majority we are returning -1)")
