# https://www.geeksforgeeks.org/find-element-appears-array-every-element-appears-twice/

# Hash Table
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i

# 2∗(a+b+c)−(a+a+b+b+c)=c
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

# Bit Manipulation
# XOR bitwise operation
# a) XOR of a number with itself is 0.
# b) XOR of a number with 0 is number itself.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
