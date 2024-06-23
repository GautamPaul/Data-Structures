class Stack:
    def __init__(self, size=10):
        self.size = size
        self.stack = []


def main():
    stack = Stack(5)
    print(stack.size)

if __name__ == "__main__":
    main()