"""
Problem:
        Given list of integers and target value, find the indices of the two different integers whosse sum is equal to target.
        !! Same elements cannot be used twice.
Approach:
        I use a dictionary to store numbers I have already seen along with
        their indices. For each number, I calculate the value needed to reach
        the target. If that value is already in the dictionary, I return both
        indices. Otherwise, I store the current number in the dictionary.
Time Complexity:
        O(n) because I traverse the list once.
Space Complexity:
        O(n) because I use a dictionary to store elements.
"""
def two_sum(nums, target):
    seen = {}  # stores number>>>index
    for i, num in enumerate(nums):
        required = target - num
        if required in seen:
            return [seen[required], i]
        seen[num] = i
# print(two_sum([2,7,11,15], 9))
