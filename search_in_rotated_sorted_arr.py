# https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/587261/Python-recursion-O(log-n)-11-lines-easy-to-understand

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def helper(l, h):
            if l > h:
                return -1

            mid = (l + h) // 2
            if nums[mid] == target:
                return mid

            # follow left half if left is sorted and target is in its range
            # or right is sorted but target not in its range
            if nums[l] <= target < nums[mid] or (nums[mid] <= nums[h] and not nums[mid] < target <= nums[h]):
                return helper(l, mid - 1)
            else:
                return helper(mid + 1, h)

        return helper(0, len(nums) - 1)