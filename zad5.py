def sprawdzanie_listy(lista, wartosc):
    wynik = wartosc in lista
    return wynik

lista = [1, 2, 3, 4, 5]
wynik_sprawdzenia = sprawdzanie_listy(lista, 3)
print(wynik_sprawdzenia)
