def czy_parzysta(liczba):
    wynik = liczba % 2 == 0
    if wynik:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
    return wynik

wynik=czy_parzysta(7)
