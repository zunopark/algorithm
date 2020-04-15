n,m = map(int, input().split())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# LinkedList 클래스 (자료구조) 정의
class DLL:
    def __init__(self):
        self.head = Node('head')
        self.result = []
    
    def find(self, value):
        current = self.head
        while current.data != value:
            current = current.next
        
        return current
    
    def insert(self, value, bool):
        if bool:
            current = self.head
            new_node = Node(value)
            while current.next != None:
                current = current.next
            new_node.next = self.head.next
            current.next = new_node
            new_node.prev = current
        else:
            current = self.head
            new_node = Node(value)
            while current.next != None:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            new_node.prev = current


    
    def show(self):
        current = self.head
        cnt = 0
        while current.next != None:
            if cnt == 14:
                break
            cnt += 1
            print(current.data, end="->")
            current = current.next
        print(current.data)
    
    
    def remove(self, m):
        current_node = self.head
        cnt = 0

        while True:
            if cnt == n:
                break

            for i in range(m):
                if current_node.next == None:
                    current_node = self.head.next
                else:
                    current_node = current_node.next
            
            self.result.append(current_node.data)
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            
            
            cnt += 1
            


queue = DLL()

for i in range(1, n+1):
    if i == n:
        queue.insert(i, True)
    else:
        queue.insert(i, False)


queue.remove(m)
print('<', end="")
for i in range(len(queue.result)):
    if i == len(queue.result)-1:
        print(queue.result[i], end=">")
    else:
        print(queue.result[i], end=", ")
        