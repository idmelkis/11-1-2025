# Uzdevums: Aprēķināt faktoriāli lietotāja ievadītajam (!) skaitlim.
# Faktoriālis - reizinājums visiem skaitļiem no 0 līdz n (piem 3! = 1*2*3=6)
#n = int(input("Ievadat skaitli: "))
n = 5
rezultats = 1
for skaitlis in range(1, n+1):
    rezultats *= skaitlis # ekvivalents `rezultats = rezultats * skaitlis`
# vai ar while ciklu
rezultats = 1
while n > 0:
    rezultats *= n
    n -= 1

# Uzdevums - uzrakstīt funkciju, kas rekursīvi aprēķina faktoriāli
def faktorialis(skaitlis :int) -> int:
    if skaitlis == 1:
        return 1
    else:
        return skaitlis * faktorialis (skaitlis - 1)
print(faktorialis(5))

saraksts = [ 123, 456 ]
print(saraksts[1])

atslēga = "mainīgā-atslēga"

# Vārdnīcas - 
vārdnīca = {
    'atslēga': 'vērtība',
    0: 'nulle',
    1: 'viens',
    atslēga: "kaut kāda vētība",
}

# Piemērs - glabāt lietotājvārdu un paroli
lietotājs1 = {
    "lietotājvārds": "ASD",
    "parole": "parole3"
}
lietotājs2 = {
    "lietotājvārds": "ASD",
    "parole": "parole2"
}
def iegūt_paroli(lietotāja_vārdn: dict) -> str:
    return lietotāja_vārdn["parole"]
print(iegūt_paroli(lietotājs1))
print(iegūt_paroli(lietotājs2))

# Piemērs - skolēna e-klase
skolēns = {
    "atzīmes": {
        "Matemātika": [ 1, 2, 5, 7],
        "Programmēšana": [ 4, 5, 10]
    },
    "vēstules": [
        {
            "autors": "Jānis",
            "ziņa": "..."
        },
        {
            "autors": "Pēteis",
            "ziņa": "..."
        }
    ]
}

print(vārdnīca['atslēga'])
print(vārdnīca[0])
print(vārdnīca[1])
print(vārdnīca["mainīgā-atslēga"])
print(vārdnīca[atslēga])


# Datu tips, kas līdzīgi, kā saraksti glabā vairākas vērtības
# dati tiek glabāti formātā - atslēga<->vērtība. Izmanto, lai glabātu
# struktuētus datus. piemērs - datu bāzes

# Piemērs: Izmantot vārdnīcas lai pārveidotu tekstā burtus āēīū formā bez
# garumzīmes, t.i. aeiu
teksts = "Māja"
pārveidotais_teksts = ""
# Ar if - ļoti garš
# for b in teksts:
#     if b == "ā":
#         pārveidotais_teksts += "a"
#     elif b == "ē"
#         pārveidotais_teksts += "e"
#     else:
#         pārveidotais_teksts += b
burti = {
    "ā": "a",
    "ē": "e",
    "ū": "u",
    "ī": "i"
}
# Pārbauda, vai sarakstā burti eksistē burts, ja eksistē,
# izmanto vērtību kas atbilst šim burtam
for b in teksts:
    # Vārdnīcās in pārbauda, vai eksistē atslēga
    if b in burti:
        pārveidotais_teksts += burti[b]
    else:
        pārveidotais_teksts += b

# Sarakstos in pārbauda vērtību
saraksts = [ "a" ]
if "a" in saraksts:
    print(True)

burti = {
    "ā": "a",
    "ē": "e",
    "ū": "u",
    "ī": "i"
}
print(burti.keys())
print(burti.values())
if "a" in burti.values():
    print(True)
print(burti.items())
for atsl, vērt in burti.items():
    print(f"Atslēga: {atsl}, Vērtība: {vērt}")
    #print("Atslēga: ", atsl, "Vērtība: ", vērt)

# Piem. Dota vārdnīca. Izvadat visu infomāciju par lietotāju.
# Izmantojat for ciklu.
vārdnīca = {
    "Lietotājvārds": "Jānis",
    "Parole": "parole1",
    "Vecums": 18,
    "Reģistrācijas datums": "2025-01-01 10:00:00TGMT-2"
}
print("Informācija par lietotāju: ")
for atsl, vērt in vārdnīca.items():
    print(f"{atsl}: {vērt}")

# Uzdevums: Dota vārdnīcas. Uzrakstat funkciju, kas pieņem vārdnīcu, un izvada visas vērtības reizinātas * 2. Izvēlēties pareizo funkciju:
# vardn.keys()
# vardn.values()
# vardn.items()
vardn = {
  0: 10,
  2: 34,
  3: 56,
  "teksts": 67
}
vardn2 = {
  0: 55,
  2: 99,
  3: 1,
  "teksts": 5
}

def reizināšana(vārdnīca :dict) -> None:
    for iii in vārdnīca.values():
        print(iii * 2)
reizināšana(vardn)
print()
reizināšana(vardn2)

saraksts = []
saraksts.append("vērtība")
#saraksts[2] = 20 # Kļūda
# Pievienošana sarakstam
vārdnīca = {
}
# 1. variants - update funkcija
vārdnīca.update({ "atslēga": "vērtība", "atslēga1": "vērtība2" })
print(vārdnīca)
vārdnīca.update({ "atslēga": "kaut kas jauns"})
print(vārdnīca)
# 2. variants 
vārdnīca["neeksistējoša atslēga"] = 10
print(vārdnīca)
vārdnīca["neeksistējoša atslēga"] = 99
print(vārdnīca)

# Uzdevums
# Uzrakstīt programmu, kas izveido vārdnīcu, kurā atslēgas 
# ir skaitļi no 1 līdz n (lietotāja ievadīts skaitlis)
# un vērtības ir šis skaitlis kvadrātā.
def kvadrats():
    n = int(input("Skaitlis: "))
    vardnica = {}
    for iii in range(n+1):
        vardnica.update({iii: iii * iii})
        # vardnica[iii] = iii * iii
    return vardnica

print(kvadrats())
print(kvadrats())

# Dzēšana no saraksta