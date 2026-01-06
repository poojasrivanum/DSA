"""
Problem:
Given a list of integers provided by the user, reverse the array
in-place.

Approach:
This problem uses the two-pointer swap pattern.
I place one pointer at the beginning of the array and another at
the end. I swap the elements at these positions and move the
pointers inward until they meet.

Time Complexity:
O(n) because each element is visited once.

Space Complexity:
O(1) because the array is reversed in-place.
"""

def reverse_array(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


--- USER INPUT HANDLING----
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))

reverse_array(nums)
print("Reversed array:", nums)
