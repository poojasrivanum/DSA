"""
Problem:
Given a list of integers and an integer k, find the total number
of continuous subarrays whose sum equals k.

Approach:
This problem uses the prefix sum + hashmap pattern.
I maintain a running prefix sum while traversing the array.
For each index, I check whether (current_prefix_sum - k)
has appeared before. If it has, it means there exists a subarray
ending at the current index whose sum is k.
I store the frequency of each prefix sum in a hashmap.

Time Complexity:
O(n) because the array is traversed once.

Space Complexity:
O(n) because a hashmap is used to store prefix sums.
"""

def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}  # base case

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]

        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count


# ---- USER INPUT HANDLING ----
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))
k = int(input("Enter value of k: "))

result = subarray_sum(nums, k)
print("Number of subarrays with sum k:", result)

