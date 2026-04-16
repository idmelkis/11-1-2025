# Iepriekšējās stundas i/ni darba risinājums
with open("ini.ignored", "r", encoding="UTF-8") as faila_mainigais:
    a = 0
    b = 0
    for line in faila_mainigais:
        if a == 0:
            a = int(line.split(" = ")[1].strip())
        elif b == 0:
            b = int(line.split(" = ")[1].strip())
        else:
            if "-" in line:
                print(a-b)
            elif "/" in line:
                print(a/b)
            elif "*" in line:
                print(a*b)
            elif "+" in line:
                print(a+b)
            a = 0
            b = 0

import os
# Nodrošina, ka faili un mapes veido tur pat kur ir .py fails
os.chdir(os.path.dirname(__file__))
# Pārbauda vai eksistē mape. Pieņem gan absolūtos, gan relatīvos ceļus.
#print(os.path.isdir("C:\\Users\\idmelkis\\Desktop\\..\\Desktop\\11-1-2025\\ignored"))
#Mapju izveide - Izveido vienu mapi
# if not os.path.exists("C:\\Users\\idmelkis\\Desktop\\..\\Desktop\\11-1-2025\\ignored"): # Ja neeksistē mape - izveidojam mapi
#     os.mkdir("C:\\Users\\idmelkis\\Desktop\\..\\Desktop\\11-1-2025\\ignored")  # Ja mape jau eksistē - tiks izmesta kļūda
#     #os.makedirs("ignored/ignored1/ignored2/ignored3") # Izveido vairākas mapes
# else:
#     print("Mape jau eksistē!")

# Mapju un failu dzēšana
# 1. Variants - manuāli iztīram mapi no failiem un izdzēšam šo mapi
# Failu dzēšana - obligāti jādara ja gribam dzēst mapi
# for file in os.listdir("ignored"): # Ejam pāri katram failam mapē
#     print(f"Dzēšam '{file}'")
#     # Dzēšam failu - mapes nosaukums jāpieliek pie faila manuāli
#     os.remove("ignored\\"+file)
# # Mapju dzēšana - izdzēš mapi - ja tā eksistē - ! un ja tā ir tukša
# os.rmdir("ignored")

# 2. Variants
import shutil
# shutil.rmtree("ignored") # Izdzēš mapi ar visiem failiem tajā

# Uzdevums: Uzrakstat programmu kura izveido mapi "mape"
# Mapē izveidojat failus ar nosaukumiem no 1 līdz 100
if not os.path.exists("mape"):
    os.mkdir("mape")
for iii in range(1,101):
    with open(f"mape\\{iii}", "w", encoding="UTF-8"):
        pass
#shutil.rmtree("mape")
# Uzdevums: Papildināt iepriekšējo programmu - izdzēst katru trešo failu
# no mapes "mape"
faili = os.listdir("mape")
for iii in range(0, len(faili), 3):
    os.remove(f"mape\\{faili[iii]}")

# Uzdevums: Izmainīt iepriekš rakstīto programmu - kādā no failiem (nejauši izvēlētā)
# ierakstīt nejaušu skaitli. Izvadīt faila nosaukumu - un lietotājam ir jāievada
# skaitlis kas ir šajā failā.
import random
# Lai iegūtu nejaušu vērtību no saraksta - varat izmantot random.choice()
#random.choice(<saraksts>)
faili = os.listdir("mape")
fails = random.choice(faili)
vertiba = random.randint(0, 100)
with open(f"mape\\{fails}", "w", encoding="UTF-8") as faila_main:
    faila_main.write(str(vertiba))
ievade = input(f"Ievadat skaitli no faila {fails}: ")
if int(ievade) == vertiba:
    print("OK!")