import linkedinlist

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = linkedinlist.fill_list([1, 2, 4])
list2 = linkedinlist.fill_list([1, 3, 4])
        
class Solution:
    def mergeTwoLists(self, list1, list2):
        tmp = []
        while list1:
            tmp.append(list1.data)
            list1 = list1.next
        while list2:
            tmp.append(list2.data)
            list2 = list2.next
        
        tmp = sorted(tmp)
        print(tmp)
        if len(tmp) > 0:
            merged = ListNode(tmp[0])
            for i in range(1, len(tmp)):
                # print(tmp[i])
                merged.next = ListNode(tmp[i])
                merged = merged.next
            
            return merged

america = Solution().mergeTwoLists(list1, list2)
print(america.val)
while america.next:
    america = america.next
    print(america.val)