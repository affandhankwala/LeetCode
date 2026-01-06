### 21 EASY
### STATUS: SOLVED
### BEATS: 100%
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            if not list2:
                return None
            return list2
        if not list2:
            return list1

        merged = merged_head = None
        pointer1, pointer2= list1, list2
        while pointer1 or pointer2:
            if pointer1:
                if pointer2:
                    # Compare value with pointer2
                    if pointer1.val <= pointer2.val:
                        # See if we have begun merged list
                        if merged:
                            merged.next = pointer1
                            merged = merged.next
                        else:
                            merged = merged_head = pointer1
                        pointer1 = pointer1.next
                    else:
                        if merged:
                            merged.next = pointer2
                            merged = merged.next
                        else:
                            merged = merged_head = pointer2
                        pointer2 = pointer2.next
                else:
                    # No pointer2
                    # merged_head is defined by now
                    merged.next = pointer1
                    return merged_head
            else:
                # No pointer1
                merged.next = pointer2
                return merged_head
        return merged_head