
#A: Head of the Linked list
#m: start of the list to be reversed
#N: end of the sublist to be reversed
def reverseLinkedList(self, A, m, N):
        head = A
        if head == None or head.next == None:
            return head
        node0 = ListNode (0)
        node0.next = head
        curr_head = node0
        for i in range (m - 1 ):
            curr_head = curr_head.next
        p = curr_head.next
        for i in range (N - m):
            tmp = curr_head.next
            curr_head.next = p.next
            p.next = p.next.next
            curr_head.next.next = tmp
        return node0.next