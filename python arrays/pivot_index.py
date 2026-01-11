"""
Problem:
Given a list of integers, find the pivot index.
The pivot index is the index where the sum of all elements
to the left is equal to the sum of all elements to the right.
If no such index exists, return -1.

Approach:
This problem uses the prefix sum pattern.
First, I calculate the total sum of the array.
Then I traverse the array while maintaining a running left sum.
At each index, the right sum can be calculated as:
right_sum = total_sum - left_sum - current_element
If left_sum equals right_sum, that index is the pivot index.

Time Complexity:
O(n) because the array is traversed once.

Space Complexity:
O(1) because no extra space is used.
"""

def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]

    return -1


# ---- USER INPUT HANDLING ----
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))

result = pivot_index(nums)
print("Pivot index:", result)

