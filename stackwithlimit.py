class stack:
    def __init__(self,stacksize):
        self.stacklist = []
        self.stacksize= stacksize
        
    def isfull(self):
        if len(self.stacklist)== self.stacksize:
            return True
        else:
            return False

    def push(self, value):
        if self.isfull():
            print("STACK IS FULL")
        else:
            self.stacklist.append(value)

    def show(self):
        print("Stack elements:", self.stacklist)

    def isEmpty(self):
        return len(self.stacklist) == 0

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stacklist.pop()

    def deletestack(self):
        self.stacklist.clear() 
        return "Stack is deleted"

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stacklist[-1]  # Added missing 'return' keyword
size=int(input("enter the size of stack:"))
stackobj = stack(size) #stack has created

while True:
    print("\n1. Push element in stack")
    print("2. Display stack elements")
    print("3. Pop element")
    print("4. Delete stack")
    print("5. Peek")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        val = int(input("Enter the value for stack: "))
        stackobj.push(val)
    elif choice == 2:
        stackobj.show()
    elif choice == 3:
        print("Popped:", stackobj.pop())
    elif choice == 4:
        print(stackobj.deletestack())
    elif choice == 5:
        print("Top element:", stackobj.peek())
    elif choice == 6:
        print("Stack empty status:", stackobj.isEmpty())
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
        
