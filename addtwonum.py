class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # A dummy node to start the result list
        current = dummy
        carry = 0

        # Loop until both lists are exhausted
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10  # Carry for the next digit
            current.next = ListNode(total % 10)  # Create new node for this digit

            current = current.next  # Move to next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next  # The result starts after dummy