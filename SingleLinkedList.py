class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.length = 0

    def append(self, value):
        """Add a new node with the given value at the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
        
    def prepend(self, value):
        """Add a new node with the given value at the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def display(self):
        """Print all node values in the list."""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    

    def to_list(self):
        """Convert the linked list into a regular Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def search(self, value):
        """Check whether a value exists in the list."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def get(self, index):
        """Return the value of the node at the given index (0-based)."""
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp.value
            count += 1
            temp = temp.next
        return None

    def insert_at(self, index, value):
        """Insert a new node with the given value at a specific index."""
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        
        curr = self.head
        count = 0
        while curr.next:
            if count == index - 1:
                new_node.next = curr.next
                curr.next = new_node
                self.length += 1
                return
            count += 1
            curr = curr.next
        

    def update_at(self, index, value):
        """Update the value of the node at the specified index."""
        curr = self.head
        count = 0
        while curr:
            if count == index:
                curr.value = value
                return
            count += 1
            curr = curr.next

    def delete_head(self):
        """Remove the first node (head) of the list."""
        if self.head:
            self.head = self.head.next
            self.length -=1

    def delete_tail(self):
        """Remove the last node (tail) of the list."""
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        self.length -= 1


    def delete_value(self, value):
        """Delete the first node that contains the given value."""
        curr = self.head
        if self.head.value == value:
            self.head = self.head.next
            return
        
        while curr and curr.next:
            if curr.next.value == value:
                curr.next = curr.next.next
                self.length -=1
                return
            curr = curr.next
        


    def reverse(self):
        """Reverse the linked list in-place."""
        prev = None
        curr = self.head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def swap_nodes(self, value1, value2):
        """Swap nodes that contain the given two values."""
        if value1 == value2:
            return
        
        curr = self.head
        prev1 = prev2 = None
        node1 = node2 = None
        while curr and curr.next:
            if not node1 and curr.next.value == value1:
                prev1 = curr
                node1 = curr.next
            elif not node2 and curr.next.value == value2:
                prev2 = curr
                node2 = curr.next
            curr = curr.next
            
        if self.head.value == value1:
            node1 = self.head
        elif self.head.value == value2:
            node2 = self.head
        if not node1 or not node2:
            print("One or both values not found.")
            return
        
        if self.head == node1:
            self.head = node2
        elif self.head == node2:
            self.head = node1
        if prev1:
            prev1.next = node2
        if prev2:
            prev2.next = node1
            
        node1.next, node2.next = node2.next, node1.next

    def remove_duplicates(self):
        """Remove duplicate values from the list."""
        not_dupli = set()
        curr = self.head
        prev = None
        
        while curr:
            if curr.value in not_dupli:
                prev.next = curr.next
                self.length -=1
            else:
                not_dupli.add(curr.value)
                prev = curr
            curr = curr.next

    def kth_from_end(self, k):
        """Return the value of the k-th node from the end of the list."""
        length = self.length
        if k > length or k <= 0:
            return None
        
        index = length - k
        curr = self.head
        
        while index:
            index -= 1
            curr = curr.next
        return curr.value

    def middle(self):
        """Return the value of the middle node in the list."""
        length = self.length
        midd = length // 2
        curr = self.head
        
        while midd:
            midd -= 1
            curr = curr.next
            
        return curr.value

    def rotate(self, num_rotate):
        """Rotate the list to the right by the given number of positions."""
        if not self.head or num_rotate == 0:
            return
        
        length = self.length
        num_rotate = num_rotate % length
        
        if num_rotate == 0:
            return
        
        skip = length - num_rotate - 1
        curr = self.head
        
        for _ in range(skip):
            curr = curr.next
            
        new_head = curr.next
        curr.next = None
        tail = new_head
        
        while tail.next:
            tail = tail.next
            
        tail.next = self.head
        self.head = new_head
     
     
     
     
        
    def is_empty(self):
        """Check if the list is empty."""
        return self.length == 0


    def delete_at(self, index):
        """Delete the node at a specific index."""
        if not self.head:
            print("The list is empty.")
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        if index >= self.length or index < 0:
            print("Index out of range.")
            return

        curr = self.head
        count = 0
        while count < index - 1:
            curr = curr.next
            count += 1

        if curr.next:
            curr.next = curr.next.next
            self.length -= 1

            
    def sort(self):
        "Sort the linked list in ascending order."
        values = self.to_list()
        values.sort()
        self.head = None
        self.length = 0
        for val in values:
            self.append(val)

    
    def merge(self, other):
        "Merge another linked list at the end of this list"
        if self.head is None:
            self.head = other.head
            self.length = other.length
            return
        
        if other.head is None:
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = other.head
        self.length += other.length
            
             
        



sll = SingleLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)


s22 = SingleLinkedList()
s22.append(7)
s22.append(8)
s22.append(9)
s22.append(10)
s22.append(11)
s22.append(12)




sll.display()
# s22.display()
sll.merge(s22)
sll.display()

# sll.delete_at(6)
# sll.reverse()
# print(sll.length())
# print(sll.search(10))      # True
# print(sll.search(99))      # False
# sll.prepend(0)
# print(sll.length)
# sll.insert_at(5, 9)
# sll.display()
# # sll.get
# sll.delete_head()
# sll.display() 
# sll.delete_tail()
# sll.display() 
# sll.delete_value(0)
# sll.display()
# sll.update_at(1, 99)
# sll.swap_nodes(15, 5)
# sll.remove_duplicates()
# sll.display()
# # print(sll.kth_from_end(1))
# print(sll.middle())
# print(sll.rotate(2))
# print(sll.length)
# sll.display()






            
            
            
        
        
