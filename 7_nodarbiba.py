# f(x) = x^2
# f(1) = 1^2
# f(2) = 2^2
# f(3) = 3^2
# f(4) = 4^2
def f(x):
    return x*x
print(f(1))
print(f(2))
print(f(3))
print(f(4))

def nosaukums(x, y = 5, z = 5):
    print(f"x: {x}, y: {y}, z: {z}")
    return 0
#mainīgais = nosaukums(1, 2, 3)
mainīgais = nosaukums(1, z=2)
print(mainīgais)
# ievade = input()

#print(1,2,3,4,5,6,7,78,9,0)
def funkcija(*mainigais):
    print(mainigais)
    print(mainigais[4])
    # mainigais[2] = 10 # Nestrādās - mainigais ir kortežs (Tuple)
funkcija(0,1,2,3,4,5,6,7,8)

def funkcija1():
    return 999
def funkcija2(x):
    print(x)
funkcija2(funkcija1())

def funkcija1():
    # def funkcija2():
    #     print("!")
    # funkcija2()
    return 777
print(funkcija1())

kaut_kads_mainigais = 11
def funkcija():
    # global kaut_kads_mainigais # Ļauj piekļūt mainīgajiem āpus funkcijas, bet nav ieteikts šādi darīt
    mainigais_funkc = 10
    print(mainigais_funkc)
    #print(kaut_kads_mainigais)
    kaut_kads_mainigais = 12
    print(kaut_kads_mainigais)
funkcija()
print(kaut_kads_mainigais)

print()
kaut_kads_mainigais = 11
def funkcija_param(kaut_kads_mainigais):
    print(kaut_kads_mainigais)
    kaut_kads_mainigais = 12
    print(kaut_kads_mainigais)
    return kaut_kads_mainigais
kaut_kads_mainigais = funkcija_param(kaut_kads_mainigais)
print(kaut_kads_mainigais)

def funkcija_ar_typedef(mainigais: str) -> str:
    """
    Šeit ir apaksts - ko dara funkcija  
    Jaunā rindā tekstu var dabūt iepriekšējā rindā pieliekot galā 2x atstarpes  
    asdasda
    """
funkcija_ar_typedef(10)

# Uzdevums: Uzrakstīt funkciju, kas pieņem bezgalīgu daudzumu
# skaitļus kā parametrus, un izvada lielāko skaitli
# Neizmantot iebūvētās python matemātiskās funkcijas (max())
# def lielakais_skaitlis_saraksts(skaitli :list[int]):
#     lielakais_skaitlis = skaitli[0]
#     for iii in skaitli:
#         if lielakais_skaitlis < iii:
#             lielakais_skaitlis = iii
#     return lielakais_skaitlis
# print(lielakais_skaitlis_saraksts([10,20,30,10,60,10,30,40]))
# Šis variants ir tuvāk uzdevuma nosac. - skaitļi kā individuāli parametri
def lielakais_skaitlis(*skaitli :tuple[int]):
    lielakais_skaitlis = skaitli[0]
    for iii in skaitli:
        if lielakais_skaitlis < iii:
            lielakais_skaitlis = iii
    return lielakais_skaitlis
print(lielakais_skaitlis(10,20,30,10,60,10,30,40))
print(lielakais_skaitlis(90, 10, 20, 4))

# Uzdevums: Uzrakstīt funkciju, kas pieņem bezgalīgu daudzumu
# skaitļus kā parametrus, un izvada šo skaitļu reizinājumu
def skaitlu_reizinajums(*skaitli :tuple[int]):
    rezultats = 1
    for iii in skaitli:
        rezultats *= iii
    return rezultats
print(skaitlu_reizinajums(10,20,30,10,60,10,30,40))
print(skaitlu_reizinajums(90, 10, 20, 4))

# Rekursija: Funkcija, kas izsauc pati sevi
# Piemērs: Funkcija izvada skaitļus no n (ievade) līdz 0 skaitot uz leju
n = int(input("Ievade: "))
def rekursiva_funkcija(parametrs :int) -> int:
    print(parametrs)
    if parametrs > 0:
        rekursiva_funkcija(parametrs - 1)
    else: 
        return
rekursiva_funkcija(n)

# Uzdevums: Aprēķināt faktoriāli lietotāja ievadītajam (!) skaitlim.
# Faktoriālis - reizinājums visiem skaitļiem no 0 līdz n (piem 3! = 1*2*3=6)
n = int(input("Ievadat skaitli: "))
rezultats = 1
for skaitlis in range(1, n+1):
    rezultats *= skaitlis # ekvivalents `rezultats = rezultats * skaitlis`
# vai ar while ciklu
rezultats = 1
while n > 0:
    rezultats *= n
    n -= 1
# Uzdevums - uzrakstīt funkciju, kas rekursīvi aprēķina faktoriāli
