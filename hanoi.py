# Rule:
# 1. We can move only one disk at a time
# 2. We have to pick the upper disk only

import time

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print(a, "->", c)
        hanoi(n-1, b, a, c)


# Recursive solution
n = int(input("Enter disks: "))
print("\nSteps to solve Tower of Hanoi:\n")
hanoi(n, 'A', 'B', 'C')


# Class-based simulation
class Tower:
    def __init__(self):
        print("\nWelcome to Tower of Hanoi game")
        print()
        print("Given problem A = [3,2,1]  B = []  C = []")
        print("Expected output A = []  B = []  C = [3,2,1]")
        print()

        self.A = [3, 2, 1]
        self.B = []
        self.C = []

        print("Initial State:")
        self.show()

    def show(self):
        print("A =", self.A, "   B =", self.B, "   C =", self.C)
        print()

    def move(self, source, destination, s_name, d_name):
        if len(source) == 0:
            print("No disk to move from", s_name)
            return

        if len(destination) == 0 or source[-1] < destination[-1]:
            temp = source.pop()
            destination.append(temp)
            time.sleep(1)
            print(f"Moved disk {temp} from {s_name} to {d_name}")
            self.show()
        else:
            print("Invalid move!")
            print()

    def solve(self, n, source, auxiliary, destination, s_name, a_name, d_name):
        if n > 0:
            self.solve(n-1, source, destination, auxiliary, s_name, d_name, a_name)
            self.move(source, destination, s_name, d_name)
            self.solve(n-1, auxiliary, source, destination, a_name, s_name, d_name)


# Run class simulation
game = Tower()
game.solve(3, game.A, game.B, game.C, 'A', 'B', 'C')
print("Tower of Hanoi completed!")