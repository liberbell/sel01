stack = []

stack.append("United States(USA)")
stack.append("Great Britain(GBR)")
stack.append("China(CHN)")

print(stack)
stack.pop()
print(stack)

stack.append("China(CHN)")
stack.append("Russia(RUS)")
stack.append("Germany(GER")
stack.append("Japan(JPN)")
stack.append("France(FRA)")
stack.append("Italy(ITA)")
stack.append("Australia(AUS)")

print(stack.pop())
print(stack.pop())

class Stack():
    def __init__(self):
        """create a new stack"""
        self.stack = []

    def push(self, data):
        """Add an element to the stack"""
        self.stack.append(data)

    def pop(self):
        """Remove the top element of the stack"""
        if self.is_empty():
            raise Exception("Nothing to pop")
        return self.stack.pop(len(self.stack) - 1)