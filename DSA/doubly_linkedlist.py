
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    def append(self, value):
        if self.head is None: # empty doublylinkedlist
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node = Node(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
        return True 
    def pop(self):
        if self.length == 0: #edge case: empty doublylinkedlist
            return None
        elif self.length == 1: #edge case2: only 1 node
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1

            return temp
    def prepend(self, value):
        if self.length == 0: #edge case 1: empty doubly linkedlist
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else: # general case
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        return True
    def pop_first(self):
        if self.length == 0: #edge case 1: empty doubly linkedlist
            return None
        elif self.length == 1: #edge case 2: only one node in doubly linkedlist
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else: # general case
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
            self.length -= 1
            return temp
    def get(self, index):
        if index >= self.length or index < 0: # edge case: index out of range
            return None
        else: # general case: index within length
            if index  < self.length / 2:
                temp = self.head
                for _ in range(0, index):
                    temp = temp.next
                return temp
            else:
                temp = self.tail
                for _ in range(self.length -1, index, -1):
                    temp = temp.prev
                return temp
    def set_value(self, index, value):
        node = self.get(index)
        if node is not None:
            node.value = value
            return True       
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length: # edge case1: index out of range
            return None
        elif index == 0: # edge case2: index == 0
            return self.prepend(value)
        elif index == self.length: #edge case3: index == self.length
            return self.append(value)
        else: # general case: insert in the middle
            new_node = Node(value)
            pre = self.get(index - 1)
            post = self.get(index)
            pre.next = new_node
            new_node.prev = pre
            new_node.next = post
            post.prev = new_node
        self.length += 1
        return True
    def remove(self, index):
        if index < 0 or index >= self.length: #edge case: index out of range
            return None
        elif index == 0: #edge case1: first node
            temp = self.pop_first()
            self.length -= 1
            return temp
        elif index == self.length - 1: #edge case2: last node
            temp = self.pop()
            self.length -= 1
            return temp
        else: #general case: remove node in the middle
            temp = self.get(index)
            pre = self.get(index - 1)
            post = self.get(index + 1)
            pre.next = post
            post.prev = pre
            temp.next = None
            temp.pre = None
            self.length -= 1
            return temp
    def is_palindrome(self) -> bool:
        if self.length == 1: # case 1: only 1 node
            return True
        elif self.length % 2 == 0: # case 2: even number of nodes
            step = int(self.length / 2)
            head = self.head
            tail = self.tail

            for _ in range(step):
                if head.value == tail.value:
                    head = head.next
                    tail = tail.prev
                else:
                    return False
            return True
        else: # case 3: odd number of nodes
            step = int(self.length / 2)
            head = self.head
            tail = self.tail

            for _ in range(step):
                if head.value == tail.value:
                    head = head.next
                    tail = tail.prev
                else:
                    return False
            return True
    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            # update temp
            temp = current.prev
            # swap prev and next
            current.prev = current.next
            current.next = temp
            # update current
            current = current.prev
            
        
        # swap head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
    def partition_list(self, x):
        dummy1 = Node(0)
        prev1 = dummy1
        dummy2 = Node(0)
        prev2 = dummy2

        # edge case: empty list
        if self.length == 0:
            return None

        # general case
        current = self.head
        while current is not None:
            if current.value < x:
                prev1.next = Node(current.value)
                prev1 = prev1.next
            elif current.value >= x:
                prev2.next = Node(current.value)
                prev2 = prev2.next
            current = current.next
        
        # edge case:
        # pass

        prev1.next = dummy2.next
        self.head = dummy1.next
        self.tail = prev2

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.pop()
# my_doubly_linked_list.append(8)
# my_doubly_linked_list.append(9)
# my_doubly_linked_list.append(10)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(1)
my_doubly_linked_list.partition_list(x = 3)
my_doubly_linked_list.print_list()


