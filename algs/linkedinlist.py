class LinkedList:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data

    def append(self, val):
        
        while self.next:
            self = self.next

        self.next = LinkedList(val)

    @property
    def over_list(self):

        print(self.data)
        while self.next:
            self = self.next
            print(self.data)

def fill_list(data: list):
    ll = LinkedList(data[0])
    for i in range(1, len(data)):
        ll.append(data[i])

    return ll


l2 = fill_list([9, 9, 9, 9, 9, 9, 9])
l1 = fill_list([9, 9, 9, 9])

class Solution:
    def addTwoNumbers(self, l1: LinkedList, l2: LinkedList) -> LinkedList:

        drop = (l1.data + l2.data) // 10

        global ll
        ll = LinkedList((l1.data + l2.data) % 10)

        while l1.next or l2.next:
            if l1.next:
                l1 = l1.next
            else:
                l1.data = 0

            if l2.next:
                l2 = l2.next
            else:
                l2.data = 0

            ll.append((l1.data + l2.data + drop) % 10)
            drop =  (l1.data + l2.data + drop) // 10
        
        if drop != 0:
            ll.append(drop)

        return ll

Solution().addTwoNumbers(l1, l2)

ll.over_list
        