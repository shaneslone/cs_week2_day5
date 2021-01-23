# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseLinkedList(l):
    prev = None
    cur = l
    next_node = l
    while cur is not None:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    l = prev
    return l

