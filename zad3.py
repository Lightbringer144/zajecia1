
def pomnoz_przez_dwa(lista_liczb):
    wynik = []
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik

liczby = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_dwa(liczby)
print(wynik)
