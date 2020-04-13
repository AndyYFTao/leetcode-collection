# https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        curr_sum = 0
        max_len = 0

        for i in range(0, len(nums)):
            curr_sum = curr_sum + (1 if nums[i] == 1 else -1)

            # case 1: max_len has index starting at 0
            if (curr_sum == 0):
                max_len = i + 1

            # case 2: max_len has index starting after 0
            if curr_sum in hash_map:
                if max_len < i - hash_map[curr_sum]:
                    max_len = i - hash_map[curr_sum]
            else:
                hash_map[curr_sum] = i

        return max_len