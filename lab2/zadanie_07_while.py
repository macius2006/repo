n = int(input("n: "))
i = 0
if(n < 0):
    print("n musi byc nieujemna")
else:
    while (i < n):
        liczba = i
        if (i == 0):
            liczba = 0
        else:
            liczba = 2 ** liczba
        print("Python "+str(liczba))
        i = i + 1