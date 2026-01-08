"""
Problem:
Given an array of integers and a number k, rotate the array to the right
by k steps. Rotation means elements shifted out from the end appear at
the beginning.

Approach:
This problem uses a brute-force rotation pattern.
I perform the rotation one step at a time.
For each step, I store the last element, shift all other elements
one position to the right, and place the stored element at the front.
The process is repeated k times.

Time Complexity:
O(n * k) because each rotation takes O(n) time.

Space Complexity:
O(1) because the rotation is done in-place.
"""

def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # handle k > n

    for _ in range(k):
        last = nums[-1]
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last


# ---- USER INPUT HANDLING ----
n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements separated by space: ").split()))
k = int(input("Enter rotation value k: "))

rotate_array(nums, k)
print("Rotated array:", nums)
