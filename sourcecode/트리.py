class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root
    
    def insert(self, data):
        current_node = self.root
        while True:
            if data < current_node.data:
                if current_node.left != None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(data)
                    break
            else:
                if current_node.right != None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(data)
                    break
    
    def search(self, data):
        current_node = self.root
        while current_node:
            if current_node.data == data:
                print(data, end="")
                print('를 찾았습니다.')
                return
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        print('해당 데이터를 찾지 못했습니다.')


node1 = Node(1)
bst = BST(node1)

bst.insert(2)
bst.insert(10)
bst.insert(23)

