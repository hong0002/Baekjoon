import math

def minimalne_uderzenia(wzrost_kozika, wymagany_wzrost, powiekszanie_guza):
    # Oblicz różnicę między wzrostem Kozika a wymaganym wzrostem
    roznica_wzrostu = wymagany_wzrost - wzrost_kozika

    # Oblicz minimalną liczbę uderzeń, zaokrąglając w górę
    liczba_uderzen = math.ceil(roznica_wzrostu / powiekszanie_guza)

    return liczba_uderzen

# Wczytaj dane wejściowe
wzrost_kozika, wymagany_wzrost, powiekszanie_guza = map(int, input().split())

# Oblicz i wyświetl wynik
wynik = minimalne_uderzenia(wzrost_kozika, wymagany_wzrost, powiekszanie_guza)
print(wynik)
