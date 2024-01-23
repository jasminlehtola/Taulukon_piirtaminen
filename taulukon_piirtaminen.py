a = 0 
b = 0
rivi = ""

leveys = int(input("Anna leveys: "))
korkeus = int(input("Anna korkeus: "))

while a < korkeus:

    while b < leveys:
        rivi = "*" * leveys
        b = b + 1

    b = 0
    print(rivi)
    a = a + 1



luku1 = 0

leveys = int(input("Anna leveys: "))
korkeus = int(input("Anna korkeus: "))

while luku1 < korkeus:
    print(leveys * "*")
    luku1 = luku1 + 1