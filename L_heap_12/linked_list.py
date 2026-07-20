
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __eq__(self, other):
    
        if self is None or other is None:
            return False

        return all([isinstance(other, self.__class__), self.val == other.val, self.next == other.next])

    def __repr__(self) -> str:

        return f"ListNode: {{val: {self.val} -> {self.next}}}"

    def __str__(self):

        return self.__repr__()
        
class LinkedList:
    
    def __init__(self, arr=None):

        self.head = self.tail = None

        if arr is not None:
            for i in arr:
                self.add(i)

    def __eq__(self, other):
    
        return all([isinstance(other, self.__class__), self.head == other.head])

    def __repr__(self):

        return self._display(self.head)

    def __str__(self):

        return self.__repr__()
    

    def add(self, val):
    
        node = ListNode(val)

        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    @classmethod
    def _display(cls, head):

        curr = head
        s = ""

        while curr:
            s += f"{curr.val}->"
            curr = curr.next

        return s

    @classmethod
    def print_list(cls, head):

        cls._display(head)

    @classmethod
    def array_to_linked_list(cls, arr):

        if not arr:
            return None

        curr = ListNode(arr[0])
        head = curr
        i = 1

        while i < len(arr):
            curr.next = ListNode(arr[i])
            curr = curr.next
            i += 1

        return head
