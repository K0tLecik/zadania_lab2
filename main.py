import sys as system
import math

# Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej lubiane sporty na sam koniec.

print("zadanie 1:\n")
sporty = ["kolarstwo", "pilka nozna", "koszykowka", "narciarstwo"]
sporty.reverse()
sporty.append("lyzwiarstwo")
sporty.append("bieg przelajowy")
print(sporty)
print("\n")

# Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych. Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.

print("zadanie 2:\n")
slownik = {"wyd." : "wydanie", "t." : "tom", "tłum." : "tłumacznie"}
print(slownik)
print("\n")

# Zad 3. Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co wartością w takim słowniku. Policz liczbę elementów w słowniku.

print("zadanie 3:\n")
slownik_gier = {"cs" : "counter strike", "lol" : "league of legends", "wot" : "world of tanks"}
print(len(slownik_gier))
print("\n")

# Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input

print("zadanie 4:\n")
zdanie = input("Wpisz zdanie: ")
print(zdanie.count("a"))
print("\n")

# Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: a^b + c. Użyj instrukcji readline() i write()).

print("zadanie 5:\n")
system.stdout.write("Wpisz dowolne 3 liczby: ")
a = system.stdin.readline()
b = system.stdin.readline()
c = system.stdin.readline()
a = int(a)
b = int(b)
c = int(c)
print(pow(a, b) + c)
print("\n")

# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.

print("zadanie 6:\n")
print("Wpisz 3 liczby: \n")
a = input()
b = input()
c = input()
print("Najwieksza liczba to: ")
if (a>=b) & (a>=c):
    print(a)
elif (b>=a) & (b>=c):
    print(b)
else:
    print(c)
print("\n")

# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.

print("zadanie 7:\n")
liczby = [1, 3.5, 17, 4.23, 21.37, 2.115, 9]
for x in range(len(liczby)):
    print(pow(liczby[x], 2))
print("\n")

# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.

print("zadanie 8:\n")
parzyste = []
i = 0
print("Wpisz 10 liczb: \n")
while i < 10:
    a = input()
    a = int(a)
    if a%2==0:
        parzyste.append(a)
    i+=1
print(parzyste)
print("\n")

# Zad 9. Napisz skrypt, który rysuje następującą literę

print("zadanie 9:\n")
lista = [1,2,3,4,5,6]
for x in range(5):
    if x%2==0:
        for y in range(lista[5]):
            system.stdout.write("E")
        print("\n")
    else:
        for y in range(lista[0]):
            system.stdout.write("E")
        print("\n")
print("\n")

# Zad. 10 Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.

print("zadanie 10:\n")
a = input("Podaj liczbe do spierwiastkowania: \n")
a = int(a)
if a<0:
    print("Liczba ujemna hallo policja!")
else:
    print(pow(a,1/2))