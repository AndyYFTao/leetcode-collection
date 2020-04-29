# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603207/Clean-commented-O(n)-post-order-depth-first-traversal-beats-99

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _max_path_sum(self, root: TreeNode) -> List[int]:
        # Base case, terminal null node
        if root is None:
            return float('-inf'), float('-inf')
        v = root.val
        # Base case, no children
        if root.left is None and root.right is None:
            return v, v

        best_left, best_thru_left = self._max_path_sum(root.left)
        best_right, best_thru_right = self._max_path_sum(root.right)
        best_thru = max(v + best_thru_left, v + best_thru_right, v)
        centred = v + best_thru_left + best_thru_right
        best_including = max(best_thru, centred)
        best = max(best_including, best_left, best_right)
        return best, best_thru

    def maxPathSum(self, root: TreeNode) -> int:
        best, _ = self._max_path_sum(root)
        return best