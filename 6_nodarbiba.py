#2. Uzdevums (2p)
# Izstrādājat programmu, kurā lietotājs ievada sarakstā 5 daļskaitļus. Izvadat šo sarakstu, un šo skaitļu kvadrātsaknes.
# Lai aprēķinātu kvadrātsakni var izmantot sekojošu funkciju:

def funkcija():
    mainigais = 10
    print()
funkcija()

import random
saraksts = []
for iii in range(5):
    #saraksts.append(float(input(f"Ievade {iii+1}: ")))
    saraksts.append(float(random.randint(0, 100)))

for skaitlis in saraksts:
    print(f"{skaitlis}", end=" ")
print()
import math
for skaitlis in saraksts:
    print(f"{math.sqrt(skaitlis)}", end=" ")
print()

# Uzdevums: Aprēķināt faktoriāli lietotāja ievadītajam (!) skaitlim.
# Faktoriālis - reizinājums visiem skaitļiem no 1 līdz n (piem 3! = 1*2*3=6)
ievade = int(input("Skaitlis: "))
rezultats = 1
for skaitlis in range(1,ievade+1):
    rezultats *= skaitlis # rezultats = rezultats * skaitlis
print(rezultats)