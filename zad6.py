def funkcja_listy(lista1, lista2):
    zlaczone_listy = list(set(lista1 + lista2))
    spotegowane_listy = [x ** 3 for x in zlaczone_listy]
    return spotegowane_listy

lista1 = [1, 2, 3]
lista2 = [3, 4, 5]
wynik = funkcja_listy(lista1, lista2)
print(wynik)
