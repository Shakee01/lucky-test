import random

runda = 1

def podajLiczbe():
    podaj_liczbe = int(input('Podaj liczbe: '))

    if podaj_liczbe > 100:
        print('Za duza liczba')
    elif podaj_liczbe < 0:
        print('Za mala liczba')

    return podaj_liczbe


x = 'y'

while x == 'y':

    liczba = random.randint(1, 100)

    def poprawnaLiczba():
        print('Poprawna odpowiedz to', liczba)

    liczba_gracza = podajLiczbe()

    if liczba_gracza == liczba:
        print('BRAWO!!! Trafiles')
        poprawnaLiczba()
        print('\nTrafiles w probie', runda, '\n')
    else:
        print('Nie trafiles')
        poprawnaLiczba()
        runda += 1
        print('\nAktualna proba to', runda, '\n')

    x = input('Jesli chcesz sprobowac jeszcze raz napisz y, jezeli nie napisz n: ')
    print('\n')