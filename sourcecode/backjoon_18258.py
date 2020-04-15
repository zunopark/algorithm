class queue:
    def __init__(self):
        self.qu = []
    
    def push(self, data):
        self.qu.append(data)
    
    def pop(self):
        if self.size() == 0:
            return -1
        else:
            temp = self.qu[0]
            self.qu.remove(self.qu[0])
            return temp

    def size(self):
        return len(self.qu)
    
    def empty(self):
        if len(self.qu):
            return 0
        else:
            return 1
    
    def front(self):
        if self.size() == 0:
            return -1
        else:
            return self.qu[0]
    
    def back(self):
        if self.size() == 0:
            return -1
        else:
            return self.qu[-1]



n = int(input())

qu = queue()

for i in range(n):
    temp = input().split()
    if "push" in temp:
        qu.push(temp[1])
    elif "pop" in temp:
        print(qu.pop())
    elif "size" in temp:
        print(qu.size())
    elif "empty" in temp:
        print(qu.empty())
    elif "front" in temp:
        print(qu.front())
    elif "back" in temp:
        print(qu.back())
