from queue import Queue

olympics = Queue(5)
print(olympics)

olympics.put("United States(USA)")
olympics.put("Great Britain(GBR)")

print(olympics.empty())
print(olympics.full())

print(olympics.qsize())

olympics.put("China(CHN)")
olympics.put("Russia(RUS)")
olympics.put("Germany(GER)")

print(olympics.full())

print(olympics.qsize())
print(olympics.get())
print(olympics.qsize())

print(olympics.get())
print(olympics.get())
print(olympics.qsize())

print(olympics.get())
print(olympics.get())
print(olympics.empty())
# print(olympics.get())

class MyQueue:
    def __init__(self):
        """create a new queue,"""
        self.items = []

    def is_empty(self):
        """return true if queue is empty"""
        return len(self.items) == 0

    def enqueue(self, item):
        """add a new element to the end of queue."""
        self.items.append(item)

    def dequeue(self):
        """remove a element from the beginning of queue."""
        return self.items.pop(0)