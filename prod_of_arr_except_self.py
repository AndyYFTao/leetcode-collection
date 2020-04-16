# https://www.geeksforgeeks.org/a-product-array-puzzle/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        prod = [1 for i in range(n)]

        # left-side product
        temp = 1
        for i in range(n):
            prod[i] = temp
            temp *= nums[i]
        # right-side product
        temp = 1
        for i in range(n - 1, -1, -1):
            prod[i] *= temp
            temp *= nums[i]

        return prod 