# https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversal-set-2/?ref=rp

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        # The first element of pre[] is always root
        root = TreeNode(preorder[0])
        size = len(preorder)

        s = []

        # append root
        s.append(root)

        i = 1

        # Iterate through rest of the size-1
        # items of given preorder array
        while (i < size):
            temp = None

            # Keep on popping while the next value
            # is greater than stack's top value.
            while (len(s) > 0 and preorder[i] > s[-1].val):
                temp = s.pop()

                # Make this greater value as the right child
            # and append it to the stack
            if (temp != None):
                temp.right = TreeNode(preorder[i])
                s.append(temp.right)

                # If the next value is less than the stack's top
            # value, make this value as the left child of the
            # stack's top node. append the new node to stack
            else:
                temp = s[-1]
                temp.left = TreeNode(preorder[i])
                s.append(temp.left)
            i = i + 1

        return root