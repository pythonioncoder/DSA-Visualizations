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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # appending is O(1) due to the simple changing of tail pointer
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # popping is O(n) because you need to iterate through the list to find the second to last value
        if self.head is None:
            return None
        elif self.length == 1:
            right = self.head
            self.head = None
            self.tail = None
        else:
            left, right = self.head, self.head.next
            while right is not self.tail:
                left = left.next
                right = right.next
            self.tail = left
            self.tail.next = None
        self.length -= 1
        return right

    def prepend(self, value):
        # O(1)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.length += 1
        return True

    def pop_first(self):
        # O(1) since the second element is easily accessible
        temp = self.head
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        # O(n)
        if index < 0 or index >= self.length:
            return None

        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        # O(n) to iterate through the list
        left = self.get(index-1)
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        elif left:
            new_node = Node(value)
            new_node.next = left.next
            left.next = new_node
            self.length += 1
            return True
        return False

    def remove(self, index):
        # O(n) to find item
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        elif index < 0 or index >= self.length:
            return None
        left = self.get(index-1)
        right = left.next
        left.next = right.next
        right.next = None
        self.length -= 1
        return True

    def reverse(self):
        if self.head is None:
            return None
        elif self.length == 1:
            return True
        temp = self.head
        self.head = self.tail
        self.tail = temp
        right = temp.next
        left = None
        for _ in range(self.length):
            right = temp.next
            temp.next = left
            left = temp
            temp = right
