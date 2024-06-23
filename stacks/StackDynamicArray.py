# class for Stack
class Stack:
    # stack constructor
    def __init__(self, size=10):
        self.size = size
        self.stack = []

    # method to check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

     # method to check if stack is full
    def is_full(self):
        return len(self.stack) == self.size

    # method to get current size of stack
    def get_size(self):
        return len(self.stack)

    # method to peek the top element of the stack
    def peek(self):
        if self.is_empty():         # check if stack is empty
            print("Stack underflow. Stack is empty.")
        else:
            return self.stack[-1]   # return the value of top element of the stack

    # method to push element in the stack
    def push(self, data):
        if self.is_full():          # check if the stack is full
            self.resize()           # resize the stack
        self.stack.append(data)     # append the data in the stack

    # method to pop element from the stack
    def pop(self):
        if self.is_empty():                             # check if the stack is empty
            print("Stack underflow. Stack is empty.")
        else:
            return self.stack.pop()                     # pop the top element from stack

    # method to print data in stack
    def print_stack(self):
        print(self.stack)

    # method to resize the stack
    def resize(self):
        self.size = 2*self.size         # double the limit of the stack


def main():
    stack = Stack(5)
    stack.pop()
    stack.push(5)
    stack.print_stack()
    stack.push(1)
    print(stack.get_size())
    stack.print_stack()
    print(stack.pop())
    stack.print_stack()
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print_stack()
    print(stack.peek())
    print(stack.size)
    stack.push(6)
    print(stack.size)
    stack.print_stack()


if __name__ == "__main__":
    main()