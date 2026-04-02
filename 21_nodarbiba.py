# Dots fails: "AAABBBB" (labajā pusē) - izveidojat to ar roku
# Saturs: 
# 123
# 234
# 456
# Uzdevums: Atverat šo failu iekš python; saskaitat failā
# esošos skaitļus un izvadat rezultātu.
with open("AAABBBB.ignored", "r", encoding="UTF-8") as faila_mainigais:
    summa = 0
    for line in faila_mainigais:
        summa = summa + int(line.strip())
    print(f"Rezultāts: {summa}")
# Uzdevums: atverat šo failu iekš python, iekš Python
# izveidojat jaunu failu "kopija", un saglabājat šī faila saturu
# tajā.
with open("AAABBBB.ignored", "r", encoding="UTF-8") as faila_mainigais:
    with open("kopija.ignored", "w", encoding="UTF-8") as f2:
        for line in faila_mainigais:
            f2.write(line)
# Uzdevums: Iekš Python, izveidojat failu ar nosaukumu "tagad", 
# kas katru reizi, kad palaižat programmu pievieno pašreizējo 
# laiku faila beigās. Izmantojat doto datetime funkciju!
import datetime
#print(datetime.datetime.now())
with open("tagad.ignored", "a", encoding="UTF-8") as faila_mainigais:
    faila_mainigais.write(f"{datetime.datetime.now()}\n")

# JSON - JavaScript Object Notation
# Veids kā attēlot strukturētus datus teksta formātā
vārdnīca = {
    "messageHtml": "<div>Laiks programmēt!</div>",
    "atslēga": "vērtība",
    "True": False
}
import json
# Pārveidot vārdnīcu par tekstu
# dump string, ensure_ascii = False nodrošina ka garumzīmes/emoji u.tml. tiek pareizi kodētas
print(json.dumps(vārdnīca, ensure_ascii=False))
# Pārveidot tekstu par vārdnīcu
vārdnīca_str = '{"message":"Laiks programmēt!", "limitedAvailability": false, "skaitlis": 10}'
vārdnīca = json.loads(vārdnīca_str) # load string
print(vārdnīca)
print(vārdnīca['message'])

# Uzdevums: Dota sekojošā vārdnīca
# Programmai jāiegūst ievade no lietotāja - lietotājvārds un parole
# Un jāsaglabā šīs vērtības vārdnīcā
lietotajs = {
    "lietotājvārds": "",
    "parole": ""
}
# Saglabājat šo vārdnīcu kā lietotajs.json
lietotajs["lietotājvārds"] = input("Lietotājvārds: ")
lietotajs["parole"] = input("Parole: ")
with open("lietotajs.json", "w", encoding="UTF-8") as f:
    f.write(json.dumps(lietotajs, ensure_ascii=False))

# Nākošajā stundā - csv, mapju izveide