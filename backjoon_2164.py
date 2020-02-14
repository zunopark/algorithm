import queue

qu = queue.Queue()

def cycle(queue):
    queue.get()
    temp = queue.get()
    queue.put(temp)


n = int(input())

for i in range(1, n+1):
    qu.put(i)

while qu.qsize() > 1:
    cycle(qu)

print(qu.get())
