"""
Problem:
Given a list of integers, find the second largest distinct element
in the list. The list contains at least two elements.

Approach:
This problem uses a single-pass tracking (greedy) pattern.
I traverse the list once while maintaining two variables:
one for the largest element and one for the second largest.
When a new larger element is found, the previous largest
becomes the second largest.

Time Complexity:
O(n) because the list is traversed once.

Space Complexity:
O(1) because only constant extra space is used.
"""
def second_largest(nums):
  sec_largest=float('-inf')
  largest=float('-inf')
  for num in nums:
    if num > largest:
      sec_largest=largest
      largest=num
    elif num<largest and num>sec_largest:
      sec_largest=num
  return sec_largest
