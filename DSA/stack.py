from LinkedList import Node
from LinkedList import LinkedList

class Stack():
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def push(self, value):
        # edge case empty stack
        if self.height == 0:
            self.top = Node(value)
            self.height += 1
        else: # general case stack which has at least 1 node
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
            self.height += 1
    def pop(self):
        if self.height == 0: # edge case1: empty stack
            return None
        elif self.height == 1: #edge case2: only 1 node in stack
            temp = self.top
            self.top = None
            self.height -= 1
            return temp
        else: # general case
            temp = self.top
            self.top = self.top.next
            self.height -= 1
            temp.next = None
            return temp
    def peek(self):
        temp = self.top
        return temp
    def is_empty(self):
        if self.top is not None:
            return False
        else:
            return True
def reverse_string(string):
        # edge case: empty string
        if len(string) == 0:
            return None
        
        # push letters into stack
        new_stack = Stack(string[0]) # initialize with the first letter
        for letter_idx in range(1, len(string)): # push into stack with idx == 1 onward
            new_stack.push(string[letter_idx])
        
        # pop the stack to reverse order
        new_string = ""
        temp = new_stack.top
        while temp is not None:
            new_string += temp.value
            temp = temp.next
        return new_string
def is_balanced_parentheses(paren_string):
    # check if ( and ) are of same number
    num_of_open = paren_string.count("(")
    num_of_close = paren_string.count(")")
    if num_of_open != num_of_close:
        return False
    
    my_stack = Stack("")

    # check if ( and ) are of correct order
    for idx in range(len(paren_string)):
        if paren_string[idx] == "(":
            my_stack.push("(")
        elif paren_string[idx] == ")":
            my_stack.pop()
    
    if len(my_stack.top.value) == 0: # test if it is "", which has len == 0
        return True
    else:
        return False
def sort_stack(input_stack: Stack):
    # use an auxiliary stack to sort values
    sorted_stack = Stack(0)
    # empty the helper stack so we can use it as empty
    sorted_stack.pop()

    while not input_stack.is_empty():
        node = input_stack.pop()
        if node is None:
            break
        temp_val = node.value

        # move larger values back to input_stack
        while not sorted_stack.is_empty() and sorted_stack.top.value > temp_val:
            val = sorted_stack.pop()
            if val is None:
                break
            input_stack.push(val.value)

        sorted_stack.push(temp_val)

    # move sorted values back to input_stack
    while not sorted_stack.is_empty():
        val = sorted_stack.pop()
        if val is None:
            break
        input_stack.push(val.value)
    
class Queue():
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def enqueue(self, value):
        if self.first is None: #edge case: empty queue
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length += 1
        else: # general case
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node
            self.length += 1
    def dequeue(self):
        if self.first is None: # edge case 1: empty queue
            return None
        elif self.length == 1: # edge case 2: 1 node
            temp = self.first
            self.first = None
            self.last = None
            self.length -= 1
            return temp
        else: # general case
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -= 1
            return temp


if __name__ == "__main__":
    my_stack = Stack(2)
    my_stack.push(4)
    my_stack.push(1)
    my_stack.push(3)
    print("Stack before sort:")
    my_stack.print_stack()

    sort_stack(my_stack)

    print("Stack after sort:")
    my_stack.print_stack()
