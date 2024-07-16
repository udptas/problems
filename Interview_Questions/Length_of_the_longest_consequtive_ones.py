# Length of longest consecutive ones
# Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the
# longest consecutive 1’s that can be achieved.
# Input 1:      A = "111000"      Output 1:     3
# Input 2:      A = "111011101"   Output 2:     7


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # Handling  the corner case where all element will be 1s, i.e. there us no 0
        count = 0
        for i in range(len(A)):
            if A[i] == '1':
                count += 1
        # print(f"Count is {count} and length is {len(A)}")
        if count == len(A):
            return count

        # Handling the generic case with expansion method
        maxlength = 0
        for i in range(len(A)):
            if A[i] == '0':
                # print(A[i])
                l, r = 0, 0
                # Handling for left expansion <------'0'
                for j in range(i - 1, -1, -1):
                    # print(f"For left expansion of {i} th 0, j is {j}")
                    if A[j] == '1':
                        l += 1
                    else:
                        break
                # Handling for the right expansion '0'------>
                for j in range(i + 1, len(A), 1):
                    # print(f"For right expansion of {i} th 0, j is {j}")
                    if A[j] == '1':
                        r += 1
                    else:
                        break
                # print(f"Value of l and r are {l, r} for {i} th 0")
                maxlength = max(maxlength, l + r + 1)
        if maxlength > count:  # count means no of 1s
            return maxlength - 1
        return maxlength


s1=Solution()
A = "111011101"
print(f"For {A}, the answer is {s1.solve(A)}")
B = "111000"
print(f"For {B}, the answer is {s1.solve(B)}")
