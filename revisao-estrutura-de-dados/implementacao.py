class Pilha:
    def __init__(self):
        self.itens = []
    
    def push(self, item):
        self.itens.append(item)
    
    def pop(self):
        if not self.esta_vazia():
            return self.itens.pop()
    
    def esta_vazia(self):
        return len(self.itens) == 0

class Fila:
    def __init__(self):
        self.itens = []
    
    def enqueue(self, item):
        self.itens.append(item)
    
    def dequeue(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
    
    def esta_vazia(self):
        return len(self.itens) == 0
