class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def convert_arr_to_linked_list(arr):
    head = ListNode(arr[0], None)
    current = head
    for i in range(1, len(arr)):
        new_node = ListNode(arr[i], None)
        current.next = new_node
        current = new_node
    return head

def print_linked_list(head):
    while head:
        print(f"{head.val}, ", end=" ")
        head = head.next