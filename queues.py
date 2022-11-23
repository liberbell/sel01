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