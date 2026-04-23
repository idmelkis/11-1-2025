# Uzdevumi
# 1. Izveidojat programmu, kas izvada vai lietotāja dotais ceļš ir fails vai mape
# Ja neeksistē - jāizvada, ka ceļš neeksistē
import os
# ceļš = input("Ceļš uz failu/mapi: ")
# if os.path.isfile(ceļš):
#     print("Esat ievadījis ceļu uz failu!")
# elif os.path.isdir(ceļš):
#     print("Esat ievadījis ceļu uz mapi!")
# else:
#     print("Ceļš neeksistē")

# 2. Izvadi skaitu ar katru paplašinājumu failiem kādai lietotāja ievadītajai mapei
# cels = input("Ceļš uz failu/mapi: ")
# if os.path.exists(cels):
#     faili = os.listdir(cels)
#     paplašinājumi = {}
#     # 1. Iegūt faila paplašinājumu
#     for fails in faili:
#         paplašinājums = fails.split(".")[-1]
#         #print(paplašinājums)
#         # 2. Saskaitīt tos
#         paplašinājumi[paplašinājums] = paplašinājumi.get(paplašinājums, 0) + 1
#         # Garāks veids
#         # if paplašinājums in paplašinājumi:
#         #     paplašinājumi[paplašinājums] += 1
#         # else:
#         #     paplašinājumi[paplašinājums] = 1
#     print(paplašinājumi)
# else:
#     print("Ceļš neeksistē!")

# 3. Ir dots CSV fails - 
# [https://ayy.lv/11a.csv]
# Saturs:
# name,age,grade
# Alice,19,"[8,9,10,0]"
# Bob,20,"[9,10,4,4]"

# 1. Izvadīt vidējos vērtējumus katram cilvēkam.
import csv
import json
with open("24_nodarbiba.csv", "r", encoding="UTF-8") as fails:
    next(fails)
    reader = csv.reader(fails, quotechar="\"")
    # 2. Izvadīt vidējo vērtējumu abiem cilvēkiem
    skolenu_atzimes = [ ]
    for skolens in reader:
        atzimes = json.loads(skolens[2])
        videja_atz = sum(atzimes) / len(atzimes)
        print(videja_atz)
        skolenu_atzimes.append(videja_atz)
    kopa_videja_atz = sum(skolenu_atzimes) / len(skolenu_atzimes)
    print(kopa_videja_atz)

    # 3. Izvadi visus datus JSON(!) formātā
    fails.seek(0)
    dictReader = csv.DictReader(fails)
    for dati in dictReader:
        print(json.dumps(dati, ensure_ascii=False))

# 4. Pievieno jaunu skolēnu šim failam!
with open("24_nodarbiba.csv", "a", encoding="UTF-8") as fails:
    vards = input("Vārds: ")
    vecums = int(input("Vecums: "))
    atzimes = [] # TODO: Vairākas atzīmes
    csv_str = f"{vards},{vecums},\"{json.dumps(atzimes)}\"\n"
    fails.write(csv_str)
    # otrs variants - izmantot csv bibliotēku
    # ...
