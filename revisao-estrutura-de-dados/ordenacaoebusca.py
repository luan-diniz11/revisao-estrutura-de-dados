# Select Sort
def select_sort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]

# Quick Sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivô = lista[0]
    menores = [x for x in lista[1:] if x <= pivô]
    maiores = [x for x in lista[1:] if x > pivô]
    return quick_sort(menores) + [pivô] + quick_sort(maiores)
