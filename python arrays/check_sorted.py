"""
Problem:
Given a list of integers, determine whether the array is sorted
in non-decreasing order (each element is greater than or equal
to the previous one).

Approach:
This problem uses an order-checking with early-exit pattern.
I iterate through the array starting from the second element
and compare each element with the one before it.
If I ever find a case where the current element is smaller
than the previous one, the array is not sorted and I return False.
If the loop finishes without finding such a case, the array is sorted.

Time Complexity:
O(n) because the array is traversed once.

Space Complexity:
O(1) because no extra space is used.
"""

def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False

    return True
