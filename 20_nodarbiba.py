import os
os.chdir(os.path.dirname(__file__))

# Failu izveide, rakstīšana, atvēršana...
# Atvērt failu - vecais stils - lūdzu nelietot
#fails = open()
# ...
#fails.close()
# Atvērt failu - ieteiktais stils

# open funkcija parametri -
# 1. Faila nosaukums
# 2. Faila atvēršanas režīms
# read - r - lasīt
# write - w - rakstīt [ izveidos failu; pārraksta failu, ja tas eksistē ]
# append - a - rakstīt faila beigās [ izveidos failu; nepārraksta failu, ja tas eksistē ]
# read + append - r+ - atver failu gan rakstīšanai, gan lasīšanai - pārraksta failu
# write + read - w+ - atver failu gan rakstīšanai, gan lasīšanai - nepārraksta failu
# Ja gribat atvērt failu binārā režīmā - pievienoja b, piem "wb" - write binary
# Vairāk informācija: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# 3. Faila kodējums - ieteikums - vienmēr UTF-8
# with open("fails.ignored", "w", encoding="UTF-8") as mainiga_nosaukums:
#     print("Fails atvērts")
# print("Fails aizvērts")

with open("fails.ignored", "w", encoding="UTF-8") as faila_mainigais:
    print("Fails atvērts")
    # Rakstam failā
    #faila_mainigais.write("Vienkārši teksts!\n")

    # "vairākas rindas" - bet galā tā pat jāliek \n simbols
    #faila_mainigais.writelines(["asdas\n", "asda\n", "dasdasd\n"])
    # alternatīva - saraksta rakstīšana
    # saraksts = ["asdas", "asda", "dasdasd"]
    # for ii in saraksts:
    #     faila_mainigais.write(ii+"\n")

    # Nolasam visus datus iekš mainīgā
    #saturs = ""
    #for line in faila_mainigais:
        #print(line.strip()) # Izvadam
        #saturs += line # Saglabājam mainīgajā
    #print(saturs)
    #print(saturs[:4])

    # Nolasam pa tiešo no faila - lasīšana izmantojot kursoru
    # parametrs - par cik simboliem kursors iet pa labi no faila sākuma
    print(faila_mainigais.read(3)) # pirmie 3 simboli - asd
    print(faila_mainigais.read(3)) # nākošie 3 simboli - as\n
    print(faila_mainigais.read(3)) # nākošie 3 simboli - asd
    print()
    # Seek funkcija pārvietojas failā, parametrs - cik baitus pārvietot, un kur sākt
    faila_mainigais.seek(0,0) # Atgriež uz faila sākumu
    print(faila_mainigais.read(3)) # pirmie 3 simboli - asd
    faila_mainigais.seek(0,0) # Atgriež uz faila sākumu
    # Pārvieto kursoru uz trešo simbolu - nedrošs, jo ar UTF-8 simboliem (piem. emoji - 4 baiti) var būt dažāds izmērs baitos. Šajā gadījumā lasot izmetīs kļūdu.
    #faila_mainigais.seek(3,0) 
    print(faila_mainigais.read(3)) # 3 simboli pēc kursora - as\n
print("Fails aizvērts")

# Uzdevums: 
# Pitonā ar open funkciju izveidot failu, pieprasīt no lietotāja kādu ievadi, un ierakstat to [ievadi] failā
with open("fails.ignored", "w", encoding="UTF-8") as f:
    f.write(input())


# Nākošajā stundā: Uzdevumi, json/csv, mapju pārvalde