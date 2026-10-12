# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head):
        
        if not head:
            return None

        # Find middle node
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is the middle node

        # Break the list
        if prev:
            prev.next = None
        else:
            head = head.next

        # Create root
        root = TreeNode(slow.val)

        # Left subtree
        root.left = self.sortedListToBST(head)

        # Right subtree
        root.right = self.sortedListToBST(slow.next)

        return root