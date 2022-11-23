from queue import Queue

olympics = Queue(5)
print(olympics)

olympics.put("United States(USA)")
olympics.put("Great Britain(GBR)")

olympics.empty()