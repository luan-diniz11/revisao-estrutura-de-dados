# Implementação de uma pilha
pilha = []
pilha.append(1)  # Inserir elemento
pilha.append(2)
pilha.pop()  # Remover o último elemento (LIFO)

# Implementação de uma fila
from collections import deque
fila = deque()
fila.append(1)  # Inserir elemento
fila.append(2)
fila.popleft()  # Remover o primeiro elemento (FIFO)
