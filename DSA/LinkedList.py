from typing import Union
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1    
    def append(self, value):
        new_node = Node(value) # create a node to connect to
        if self.head is None: # edge case where there is no node
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length = self.length + 1
        return True # optional return value
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def prepend(self, value):
        if self.head is None and self.tail is None: # case 1: empty linkedlist
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else: # case 2: at least 1 node in linkedlist
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    def insert(self, index, value):
        # validate index (allow inserting at end == append)
        if index < 0 or index > self.length:
            return False

        new_node = Node(value)

        if index == 0:
            # insert at head
            new_node.next = self.head
            self.head = new_node
            if self.length == 0:
                self.tail = new_node
        elif index == self.length:
            # insert at tail (append)
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
            if self.length == 0:
                self.head = new_node
        else:
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node

        self.length += 1
        return True
    def get(self, index):
        if index < 0 or index > self.length - 1: # if index out of range, return None
            return None
        else: # case 2: at least 1 node in linkedlist
                
            # iterate to the node
            temp = self.head
            for _ in range(0, index):
                temp = temp.next
            return temp              
    def pop(self, value: Union[int, None] = None) -> Union[int, list]:
        # if no value provided: return list of nodes and clear the list
        if value is None:
            lis = []
            node = self.head
            while node is not None:
                lis.append(node)
                node = node.next
            self.head = None
            self.tail = None
            self.length = 0
            return lis

        # normal: remove the first node with matching value
        if self.length == 0:
            return None

        prev = None
        curr = self.head
        while curr is not None and curr.value != value:
            prev = curr
            curr = curr.next

        if curr is None:
            return None

        # remove head
        if prev is None:
            self.head = curr.next
            if curr is self.tail:
                self.tail = None
        else:
            prev.next = curr.next
            if curr is self.tail:
                self.tail = prev

        self.length -= 1
        return curr
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    def remove(self, index):
        if index < 0 or index >= self.length: # if index out of range return None
            return None
        
        if self.length == 0: # case 1: empty linkedlist
            return None
        elif self.length == 1 and index == 0: # case2: only one node
            self.head = None
            self.tail = None
            self.length = 0
        elif index == 0: # case 3: remove the head node:
            self.head = self.head.next
            self.length -= 1
        elif index == self.length - 1: # case 4: remove the tail node:
            pre = self.get(self.length - 2) # pre is the node before tail node
            self.tail = pre
            pre.next = None
            self.length -= 1
        else: # remove the node in the middle
            pre = self.get(index - 1) # pre is the node before index node
            pre.next = pre.next.next
            self.length -= 1
    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        prev = None
        curr = self.head
        self.tail = self.head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    def reverse_between(self, left: int, right: int):
        # reverse nodes from position left to right (1-based indices)
        if left < 1 or right < left or self.head is None:
            return None

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        # move prev to node before left
        for _ in range(left - 1):
            if prev is None:
                return None
            prev = prev.next

        # reverse sublist
        sub_tail = prev.next
        curr = sub_tail
        prev_sub = None
        for _ in range(right - left + 1):
            if curr is None:
                break
            nxt = curr.next
            curr.next = prev_sub
            prev_sub = curr
            curr = nxt

        # reattach
        prev.next = prev_sub
        sub_tail.next = curr
        # update head and tail if needed
        self.head = dummy.next
        if sub_tail.next is None:
            self.tail = sub_tail
    def swap_pairs(self):
        if self.head is None: # empty linkedlist
            return None
        elif self.head.next is None: # only one node
            return None
        else:
            dummy = Node(0) 
            dummy.next = self.head # create dummy node
            
            prev = dummy
            first = self.head    # initialize ends

            while first is not None and first.next is not None:
                second = first.next

                
                first.next = second.next
                second.next = first
                prev.next = second # swap part

                prev = first
                first = prev.next
                # update sliding window

            self.head = dummy.next
            
        
        
            
        

        

def find_kth_from_end(ll: LinkedList, k: int) -> Node:     
    slow = ll.head
    fast = ll.head
    for _ in range(k): # let fast move forward by k steps first
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow    
        
if __name__ == "__main__":
    my_linkedlist = LinkedList(1)
    my_linkedlist.append(2)
    # my_linkedlist.append(3)
    # my_linkedlist.append(4)
    # my_linkedlist.append(5)
    # my_linkedlist.append(6)
    # my_linkedlist.append(7)
    my_linkedlist.swap_pairs()
    my_linkedlist.print_list()