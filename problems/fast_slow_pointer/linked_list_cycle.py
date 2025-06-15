
def is_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

link = [3,2,0,-4]
print(is_cycle(link))
