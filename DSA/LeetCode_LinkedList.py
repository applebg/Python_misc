# Solve the following problem:
# Constraint: 1) only 1 time of iterating through the linkedlist. 2) counting the length is not allowed
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
    def append(self, value):
        new_node = Node(value) # create a node to connect to
        if self.head is None: # edge case where there is no node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    def has_loop(self):
        fast = self.head
        slow = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
    def remove_duplicates(self):
        current = self.head
        runner = self.head
        while current is not None:
            while runner is not None:
                if runner.next is None:
                    break
                elif runner.next.value == current.value:
                    runner.next = runner.next.next
                runner = runner.next
            current = current.next
            runner = current
    def binary_to_decimal(self):
        current = self.head
        sum = 0
        while current is not None: 
            sum = sum * 2 + current.value
            current = current.next
        return sum
    def partition_list(self, x:int):
        dummy1 = Node(0)
        prev1 = dummy1
        d1 = dummy1
        dummy2 = Node(0)
        prev2 = dummy2
        d2 = dummy2
        current = self.head
        while current is not None:
            if current.value < x:
                prev1.next = Node(current.value)
                prev1 = prev1.next
            elif current.value >= x:
                prev2.next = Node(current.value)
                prev2 = prev2.next
            current = current.next
        
        prev1.next = d2.next
        self.head = d1.next
        self.tail = prev2
        return self
    def reverse_between(left: int, right: int):
        pass
        
    
def kth_node_from_end(ll:LinkedList, k:int) -> Node:
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
    my_linkedlist = LinkedList(3)
    my_linkedlist.append(8)
    my_linkedlist.append(5)
    my_linkedlist.append(10)
    my_linkedlist.append(2)
    my_linkedlist.append(1)
    