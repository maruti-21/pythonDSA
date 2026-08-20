import sys
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addAtBeginning(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node                  
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addInBetween(self, value, position):
        node = Node(value)
        if position == 1:
            node.next = self.head
            self.head = node
            return
        temp = self.head
        for i in range(1, position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        node.next = temp.next
        temp.next = node

    def addAtEnd(self, value):
        self.addNode(value)

    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        while temp:
            print(f"| {temp.data} |", end=" --> ")
            temp = temp.next
        print("None")

linkedlist = LinkedList()

while True:
    print("\n1. Add node LinkedList")
    print("2. Add node at Beginning")
    print("3. Add node in Between")
    print("4. Add node at End")
    print("5. Display LinkedList")
    print("6. Exit")

    ch = int(input("Enter your choice: "))
    if ch == 1:
        val = int(input("Enter value: "))
        linkedlist.addNode(val)
    elif ch == 2:
        val = int(input("Enter value: "))
        linkedlist.addAtBeginning(val)
    elif ch == 3:
        val = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        linkedlist.addInBetween(val, pos)
    elif ch == 4:
        val = int(input("Enter value: "))
        linkedlist.addAtEnd(val)
    elif ch == 5:
        linkedlist.display()
    elif ch == 6:
        print("Exiting...")
        sys.exit
    else:
        print("Invalid choice")