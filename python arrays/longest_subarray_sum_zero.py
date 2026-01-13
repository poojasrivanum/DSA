"""
Problem:
Given a list of integers, find the length of the longest
subarray whose sum is equal to zero.

Approach:
This problem uses the prefix sum + hashmap pattern.
I maintain a running prefix sum while traversing the array.
If the same prefix sum appears again, it means the elements
between the two indices sum to zero.
I store the first occurrence of each prefix sum in a hashmap
and update the maximum subarray length whenever a prefix sum
repeats.

Time Complexity:
O(n) because the array is traversed once.

Space Complexity:
O(n) because a hashmap is used to store prefix sums.
"""

def longest_subarray_sum_zero(nums):
    prefix_sum = 0
    max_len = 0
    prefix_index = {0: -1}  # prefix sum 0 at index -1

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum in prefix_index:
            length = i - prefix_index[prefix_sum]
            max_len = max(max_len, length)
        else:
            prefix_index[prefix_sum] = i

    return max_len


# ---- USER INPUT HANDLING ----
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))

result = longest_subarray_sum_zero(nums)
print("Length of longest subarray with sum zero:", result)
