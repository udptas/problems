#  Longest Palindromic Substring
# Problem Description
# Given a string A of size N, find and return the longest palindromic substring in A.
# Substring of string A is A[i...j] where 0 <= i <= j < len(A)
# Palindrome string:
# A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
# Incase of conflict, return the substring which occurs first ( with the least starting index).
# Input Format   ::  First and only argument is a string A.
# Output Format   ::  Return a string denoting the longest palindromic substring of string A.
# Example:
#           Input 1:  A = "aaaabaaa"  Output 1: "aaabaaa"
#           Input 2:  A = "abba    Output 1: "abba"


class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        # Need to do this for both even and odd cases
        max_length = 0  # Max length is initialized to 0 so that we can compare it with palindromic shub strings
        max_str = ""  # Will save the palindromic String to return, which is the answer
        # Odd ===> This is for palindromes having Odd Length
        # Approach is keep an index as a center, l, r are two pointers which will decrement and increment respectively
        # and in every step it will try to match with A[l] and A[r], if matches will continue else calculate the last
        # string length and save it
        for c in range(len(A)):
            l, r = c, c
            # print(c, max_length)
            while l >= 0 and r <= len(A) - 1 and A[l] == A[r]:
                # print(c,r,l)
                r += 1
                l -= 1
            length = r - l - 1
            if max_length < length:
                # print(A[l+1:r])
                max_str = A[l + 1:r]
            max_length = max(length, max_length)
            # print(max_length)
        # Even ==> This is for palindromes having Even Length Approch is we are taking 2 pointers l and r,
        # at the same time , l will be always small that is why r is starting from 1 (l=0, r=1). l and r will be
        # decremented and incremented by 1  and will compare A[l] and A[r] As this will be palindrome with even
        # length. Other things are similar
        for r in range(1, len(A)):
            l = r - 1
            # print(l,r, max_length)
            while l >= 0 and r <= len(A) - 1 and A[l] == A[r]:
                l -= 1
                r += 1
            leng = r - l - 1
            # print(leng, l, r, "Test")
            if max_length < leng:
                # print(A[l+1:r])
                max_str = A[l + 1:r]
            max_length = max(leng, max_length)
        return max_str


s1 = Solution()
# input = "aaabaaa"
input = "aasabbasaadhfdjh"
ans = s1.longestPalindrome(input)
print(f"The Longest Palindromic substring in {input} is :: {ans}")

