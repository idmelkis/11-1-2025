# Uzdevums:
# Uzrakstat for ciklu, kas izvada skaitļus no 0 līdz 10,
# izlaižot skaitļus 4 un 6.
for skaitlis in range(0,11):
    if skaitlis == 4 or skaitlis == 6:
        continue
    print(skaitlis)

# Uzdevums: Uzrakstīt šo for ciklu kā while ciklu
skaitlis = -1
while skaitlis < 11:
    skaitlis += 1
    if skaitlis == 4 or skaitlis == 6:
        continue
    print(skaitlis)

# Uzdevums: Aprēķināt faktoriāli lietotāja ievadītajam (!) skaitlim.
# Faktoriālis - reizinājums visiem skaitļiem no 1 līdz n (piem 3! = 1*2*3=6)
ievade = int(input("Skaitlis: "))
rezultats = 1
for skaitlis in range(1,ievade+1):
    rezultats *= skaitlis # rezultats = rezultats * skaitlis
print(rezultats)

# Programma uzģenerē nejaušu skaitli izmantojot sekojošo kodu:
import random
skaitlis = random.randint(0, 100)
# Uzdevums: Jāuzraksta cikls, kurā lietotājs ievada skaitli.
# Programma pārbauda vai skaitlis ir uzminēts,
# ja nav, izvada, vai ievadītais skaitlis ir lielāks, vai mazāks par nejaušo skaitli.
# ja ir - cikls beidz darbu un izvada vārdu "Uzvara"
while True:
    ievade = int(input("Skaitlis: "))
    if ievade > skaitlis:
        print("Ievade ir lielāka")
    elif ievade < skaitlis:
        print("Ievade ir mazāka")
    elif ievade == skaitlis: # else
        break
print("Uzvara")


# Uzdevums:
# Uzrakstīt ciklu [for], kas iet pāri skaitļiem no 1 līdz 100, UN
# Ja skaitlis dalās ar 3, izvada vārdu "AAA"
# Ja skaitlis dalās ar 5, izvada vārdu "BBB"
# Ja skaitlis dalās ar 3 UN 5, izvada "AAABBB"
# Ja skaitlis nedalās ar nevienu no šiem skaitļiem, izvadat šo skaitli
# Dalīšanas atlikuma pārbaudei izmatot - % - modulus operatoru
# Modulus operators - izvada dalīšanas atlikumu, piem.
# 5 % 2 == 1
# 7 % 3 == 1
# Šo var izmantot lai pārbaudītu, vai skaitlis dalās ar
# citu skaitli (izvadīs 0).
# 6 % 3 == 0
# N.B. šī ir darbība - tā pat kā citas (saskaitīšana, reizināšana utt.)
# Lai pārbaudītu vērtību ir jāizmanto ==, >, < u.tt.