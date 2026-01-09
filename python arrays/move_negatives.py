"""
Problem:
Given a list of integers provided by the user, move all negative
numbers to the left side of the array. The relative order of elements
does not matter.

Approach:
This problem uses the two-pointer partition pattern.
I maintain a pointer that tracks the position where the next
negative number should be placed. While traversing the array,
whenever a negative number is found, it is swapped with the element
at the current pointer position, and the pointer is moved forward.

Time Complexity:
O(n) because the array is traversed once.

Space Complexity:
O(1) because the rearrangement is done in-place.
"""

def move_negatives(nums):
    pos = 0  # position for next negative number

    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1


# ---- USER INPUT HANDLING ----
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))

move_negatives(nums)
print("Array after moving negatives:", nums)
