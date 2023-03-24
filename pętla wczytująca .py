suma=0
licznik=0
prevNummber = None

while True :
    Liczba1 = int(input("Podaj liczbę"))
    suma = suma + Liczba1

    if Liczba1<0:
        licznik = licznik + 1
    if suma>100:
        print(suma)
        break
    if licznik>9:
        print(suma)
        break
    if Liczba1 == prevNummber:
        print(suma)
        break
    else:
              prevNummber = Liczba1
