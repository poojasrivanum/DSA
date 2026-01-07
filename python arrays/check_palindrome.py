"""
Problem:
Given a list of integers provided by the user, check whether
the array is a palindrome. An array is a palindrome if it
reads the same forward and backward.

Approach:
This problem uses the two-pointer comparison pattern.
I place one pointer at the start of the array and another
at the end. I compare the values at both pointers.
If any pair does not match, the array is not a palindrome.
If all pairs match, the array is a palindrome.

Time Complexity:
O(n) because the array is traversed once.

Space Complexity:
O(1) because no extra space is used.
"""

def is_palindrome(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1

    return True


# ---- USER INPUT HANDLING ----
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))

if is_palindrome(nums):
    print("The array is a palindrome")
else:
    print("The array is not a palindrome")
