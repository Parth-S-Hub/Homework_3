class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        root.val = sum - root.val
        nodes = [root]
        while nodes:
            curr = nodes.pop()
            if curr.val == 0 and not curr.left and not curr.right:
                return True
            if curr.left:
                curr.left.val = curr.val - curr.left.val
                nodes.append(curr.left)
            if curr.right:
                curr.right.val = curr.val - curr.right.val
                nodes.append(curr.right)
        return False

s = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)
print(s.hasPathSum(root,22))