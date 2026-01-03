"""
Problem:
Given a list of integers, move all 0 values to the end of the list
while maintaining the relative order of the non-zero elements.
The operation must be done in-place without creating a new list.

Approach:
I use a two-pointer overwrite approach. One pointer keeps track of the
position where the next non-zero element should be placed. I iterate
through the list, and whenever I encounter a non-zero value, I place
it at the current position pointer and move the pointer forward.
After processing all elements, the remaining positions are filled
with zeroes.

Time Complexity:
O(n) because the list is traversed once.

Space Complexity:
O(1) because no extra data structure is used.
"""

def move_zeroes(nums):
    pos = 0  # position for next non-zero element

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1

    # fill remaining positions with zeroes
    while pos < len(nums):
        nums[pos] = 0
        pos += 1
