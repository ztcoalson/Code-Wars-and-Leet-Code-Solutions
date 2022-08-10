def divide(nums, root):
    if len(nums) == 0:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = divide(nums[:mid], root.left)
    root.right = divide(nums[mid+1:], root.right)
    return root
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return divide(nums, None)
