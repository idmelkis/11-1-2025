# csv - ar komatu atdalītās vērtības 
# tsv - ar TABULTORU atdalītās vērtības [ izveidots nospiežot tab pogu ]
# Ļoti bieži šādiem failiem ir attiecīgs paplašinājums - .csv un .tsv
# ;, |...
##
# Simbols,Nosaukums,Suga
# ADRA1D    adrenoceptor alpha 1D   Homo sapiens
# RGS11;regulator of G protein signaling;11 Homo sapiens
# AAAA|something,somethinelse|Homo sapiens


with open("22_nodarbiba.csv", "r", encoding="UTF-8") as faila_mainigais:
    rindas = []
    # Atvērt csv failu - divi veidi
    # 1. Veids str.split()
    next(faila_mainigais) # Izlaižam pirmo rindu
    for rinda in faila_mainigais:
        sadal_rinda = rinda.strip().split(",")
        print(sadal_rinda)
        rindas.append(sadal_rinda)
    #print(rindas)
    print()
    # 2. Veids - csv bibliotēku
    import csv
    faila_mainigais.seek(0)
    # reader funkcija
    # 1. mainīgais - atsauce uz failu
    # 2. delimiter - atdalītāja simbols (standartā - komats) - neobligāti, ja dati ir atdalīti ar komatu
    # 3. quotechar - simbols, kuru izmanto lai norādītu, ka kolonā dati ir kā viens vesels
    # piem rindā - AAAA,"something,somethinelse",Homo sapiens - ir trīs, nevis četras kolonas!
    csv_reader = csv.reader(faila_mainigais, delimiter=",", quotechar="\"")
    next(csv_reader) # Izlaižam pirmo rindu
    for line in csv_reader:
        print(line)
    # Nolasīšana iekš vārdnīcas - datiem jābūt galvenei (pirmā rinda)
    # faila_mainigais.seek(0)
    # csv_dict_reader = csv.DictReader(faila_mainigais)
    # for line in csv_dict_reader:
    #     print(line)
    
# Uzdevums:
# Atverat vietni https://www.lipsum.com/
# Nokopējat tekstu zem "The standard Lorem Ipsum passage, used since the 1500s"
# Saglabājat to failā
# Iekš pitona atverat šo failu, kā csv failu (atdalītājs - atstarpe)
# Izvadīt vārdu skaitu failā (len)
with open("fails3.ignored", "r", encoding="UTF-8") as faila_mainigais:
    for rinda in faila_mainigais:
        sadal_rinda = rinda.strip().split(" ")
        print(len(sadal_rinda))

# Uzdevums i/ni:
# Manuāli izveidojat failu ar sekojošu saturu:

# A = 5
# B = 10
# C = A - B
# A = 15
# B = 3
# C = A / B
# A = 2
# B = 7
# C = A * B

# Izveidojat programmu, kas atver šo failu, 
# un izvada visas 3 C vērtības (C1, C2, C3).
# Nomainot vērtības failā, un palaižot programmu vajadzētu 
# redzēt jaunās vērtības (t.i. vērtības nedrīkst programmā vadīt ar roku).
# Pieņemt, ka programmā VIENMĒR būs šāds formāts, un tikai 3 šādas darbības.
# Kalkulatora kods: https://github.com/idmelkis/11-1-2025/blob/main/3_nodarbiba.py