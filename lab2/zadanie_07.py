n = int(input("n: "))
if(n < 0):
    print("n musi byc nieujemna")
else:
    for i in range(0,n):
        liczba = i
        if (i == 0):
            liczba = 0
        else:
            liczba = 2 ** liczba
        print("Python "+str(liczba))
        