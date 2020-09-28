from Node import Node

class stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def push(self, elem):
        #insere uma elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        #remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        else:
            raise IndexError("A pilha está vazia.")
    
    def peek(self):
        #mostra o elemento no topo da pilha
        if self._size > 0:
            return self.top.data
        else:
            raise IndexError("A pilha está vazia.")

    def __repr__(self):
        r = ""
        pointer = self.top
        while (pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__