# class for Stack
class Stack:
    # stack constructor
    def __init__(self, size=10):
        self.size = size
        self.stack = []

    # method to push element in the stack
    def push(self, data):
        if len(self.stack) == self.size:                # check if the stack is full
            print("Stack overflow. Stack is full.")
        else:
            self.stack.append(data)                     # append the data in the stack

    # method to print data in stack
    def print_stack(self):
        print(self.stack)


def main():
    stack = Stack(5)
    stack.push(5)
    stack.print_stack()
    stack.push(1)
    stack.print_stack()

if __name__ == "__main__":
    main()