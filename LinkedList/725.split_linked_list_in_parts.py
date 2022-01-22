class Solution:
    def splitListToPairs(self, head, k):
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        quotient, remainder = n // k, n % k

        parts = [None for _ in range(k)]
        i, curr = 0, head
        while i < k and curr:
            parts[i] = curr
            part_size = quotient + (1 if i < remainder else 0)
            for _ in range(part_size - 1):
                curr = curr.next
            next = curr.next
            curr.next = None
            curr = next
            i += 1

        return parts
