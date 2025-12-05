vardnica = {
    0: "viens",
    2: "divi",
    "atslēga": "vērtība"
}

# piekļūšana
print(vardnica["atslēga"])
print(vardnica.keys())
print(vardnica.values())
print(vardnica.items())
# for key, value in vardnica.items():
#     print(key, value)

# pievienošana/atjaunināšana
vardnica.update({ "jauna atsl": "jauna vērt", "jauna atsl2": "jauna vērt2" })
vardnica["neeksistējoša atslēga"] = "jauna vērt3"
print(vardnica)

# atjaunināšana
vardnica.update({ "jauna atsl2": "cita vērtība" })
vardnica["neeksistējoša atslēga"] = "????"
print(vardnica)

# dzēšana no vārdnīcas - izdzēš vērtību ar atbilstošo atslēgu
vardnica.pop("neeksistējoša atslēga")
vardnica.pop("jauna atsl")
del vardnica["jauna atsl2"]
print(vardnica)

# Uzdevums: (Dots) Tiek ģenerēts saraksts ar 20 vērtībām
# Ar ciklu izdzēst katru otro vērtību (atslēgas ir ar nepāra skaitļiem)
# Vārdnīcas garums - cik elementi (atslēgu-vērt pāri) ir vārdnīcā: len(vardnica)
import random
vardnica = {}
for iii in range(0, 20):
    vardnica[iii] = random.randint(1, 1000)
print(vardnica)

# for iii in range(len(vardnica)):
#     if iii % 2 != 0:
#         vardnica.pop(iii)
for iii in list(vardnica.keys()):
    if iii % 2 != 0:
        vardnica.pop(iii)
print(vardnica)

# Uzdevums: Ar ciklu izdzēst katru atslēgu kurai VĒRTĪBA ir pāra skaitlis
import random
vardnica = {}
for iii in range(0, 20):
    vardnica[iii] = random.randint(1, 1000)
print(vardnica)

for key, value in list(vardnica.items()):
    if value % 2 == 0:
        del vardnica[key]
        # vardnica.pop(key)

# for key in list(vardnica.keys()):
#     if vardnica[key] % 2 == 0:
#         del vardnica[key]
#         # vardnica.pop(key)

# Uzdevums: Izveidot vārdnīcu, kurā atrodas atslēgas un vērtības no dict1, 
# tām atslēgām kurām vērtības ir > 500, un izprintēt abas vārdnīcas.
# Piem, ja
# dict1 = {
#   1: 100,
#   2: 600,
#   3: 200,
#   4: 800
# }, tad
# dict2 = {
#   2: 600,
#   4: 800
# }
# Dots:
import random
dict1 = {}
for i in range(0, 20):
    dict1[i] = random.randint(0, 1000)
print(dict1)
dict2 = {}
for key, value in dict1.items():
    if value > 500:
        dict2.update({ key: value })
# # vai
# for key in dict1.keys():
#     if dict1[key] > 500:
#         dict2.update({ key: dict1[key] })
print(dict1)
print(dict2)


# i/ni uzdevums: Ir dota sekojoša vārdnīca, kurai atslēgas ir romiešu cipari
vardn = {
    'V': 0,
    'VI': 0,
    'VII': 0,
    'VIII': 0,
    'X': 0,
    'XI': 0,
    'XII': 0
}
# Uzrakstīt ciklu, kurš iet pāri visiem vārdnīcas ierakstiem, un aprēķina (!) vērtības uz atbilstošajiem arābu skaitļiem.
# Izvadīt gala vārdnīcu
# x = 'XI'
# sk = 0
# for ch in x:
#   if ch == 'X':
#     sk += 10
#   # ...