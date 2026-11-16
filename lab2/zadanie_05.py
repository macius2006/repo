pkt = int(input("Liczba punktow: "))
if(pkt >= 10):
    print("Zaliczone")
else:
    print("Niezaliczne")
    print("Barkuje "+str(10-pkt)+" pukntow")