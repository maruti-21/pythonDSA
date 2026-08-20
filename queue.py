class queue:
    def __init__(self, queuesize):
        self.queuelist = []
        self.queuesize = queuesize
        
    def isfull(self):
        return len(self.queuelist) == self.queuesize

    def enqueue(self, value):   # add element in queue
        if self.queuelist is None:
            print("Queue is deleted")
        elif self.isfull():
            print("QUEUE IS FULL")
        else:
            self.queuelist.append(value)

    def showqueue(self):
        if self.queuelist is None:
            print("Queue is deleted")
        else:
            print("Queue elements:", self.queuelist)

    def isEmpty(self):
        if self.queuelist is None:
            return True
        return len(self.queuelist) == 0

    def dequeue(self):
        if self.queuelist is None:
            return "Queue is deleted"
        elif self.isEmpty():
            return "Queue is empty"
        else:
            return self.queuelist.pop(0)

    def deletequeue(self):
        self.queuelist = None
        return "Queue is deleted"

    def peek(self):  # returns first element of queue
        if self.queuelist is None:
            return "Queue is deleted"
        elif self.isEmpty():
            return "Queue is empty"
        else:
            return self.queuelist[0]


size = int(input("Enter the size of queue: "))
queueobj = queue(size)  # queue created

while True:
    print("\n1. Enqueue element in queue")
    print("2. Display queue elements")
    print("3. Dequeue element")
    print("4. Delete queue")
    print("5. Peek operation")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        val = int(input("Enter the value for queue: "))
        queueobj.enqueue(val)
    elif choice == 2:
        queueobj.showqueue()
    elif choice == 3:
        print("Dequeued:", queueobj.dequeue())   # corrected
    elif choice == 4:
        print(queueobj.deletequeue())
    elif choice == 5:
        print("Front element:", queueobj.peek())
    elif choice == 6:
        print("Queue empty status:", queueobj.isEmpty())
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")