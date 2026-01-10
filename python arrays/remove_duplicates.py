"""
Problem:
Given a sorted list of integers, remove the duplicate elements
in-place such that each unique element appears only once.
Return the number of unique elements.

Approach:
This problem uses the two-pointer overwrite pattern.
I maintain one pointer for the position of the last unique element.
I traverse the array with another pointer, and whenever a new
unique element is found, I overwrite the next position with it.

Time Complexity:
O(n) because the array is traversed once.

Space Complexity:
O(1) because no extra space is used.
"""

def remove_duplicates(nums):
    if not nums:
        return 0

    pos = 0  # position of last unique element

    for i in range(1, len(nums)):
        if nums[i] != nums[pos]:
            pos += 1
            nums[pos] = nums[i]

    return pos + 1


# ---- USER INPUT HANDLING ----
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter sorted elements separated by space: ").split()))

k = remove_duplicates(nums)

print("Number of unique elements:", k)
print("Array after removing duplicates:", nums[:k])
