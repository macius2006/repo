liczba1 = float(input("Pierwsza liczba: "))
operacja = str(input("Operacja (+, -, *, /): "))
liczba2 = float(input("Druga liczba: "))
ok_operacja = True

if(operacja == "+"):
    wynik = liczba1 + liczba2
elif(operacja == "-"):
    wynik = liczba1 - liczba2
elif(operacja == "*"):
    wynik = liczba2*liczba1
elif(operacja == "/"):
    if(liczba2 == float(0)):
        print("Druga liczba musi byc rozna od 0")
    else:
        wynik = liczba1/liczba2
else:
    print("Zla operacja")
    ok_operacja = False
    
if(ok_operacja):
    print(wynik)