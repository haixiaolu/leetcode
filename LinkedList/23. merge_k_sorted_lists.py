from multiprocessing import dummy


class Solution:
    def mergeKLists(self, lists):
        # edge cases
        if not lists or len(lists) == 0:
            return None

        # take pair of lists and merge them until there is one list left
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeList(l1, l2))

            # one list left
            lists = merged_lists
        return lists[0]

        # helper function
        def mergeList(self, l1, l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next
