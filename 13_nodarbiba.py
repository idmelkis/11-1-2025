# Klase - abstrakcija objektiem/datiem
# mainigais = 0
# def funkcijasNosaukums():
#     mainigais = 1
# funkcijasNosaukums()
# print(mainigais)
class Nosaukums:
    # Mainīgo definīcijas
    mainigais :str = None # None - tukša vērtība
    mainigais_2 :str # str - string

    # Speciāla funkcija, 
    # kas tiek palaista izveidojot objektu
    def __init__(self, mainigais_vertiba = "Standarta vērtība"):
        self.mainigais_2 = mainigais_vertiba
        print("Teksts")
    # Speciāla funkcija, 
    # Tiek izsaukta, kad funkcija tiek pārvērsta par tekstu
    # Piemēram - ja mēs to ieliekam print funkcijā
    def __str__(self):
        return f"Mainigais1: {self.mainigais_2}"
    
    # Lietotāja definētas funkcijas
    # Piemērs - getter vai setter funkcijas
    def getMainigais(self) -> str:
        return self.mainigais
    def setMainigais(self, vertiba :str):
        if vertiba == "":
            # Izmet kļūdu
            raise Exception("Vērtība nedrīkst būt tukša")
        self.mainigais = vertiba

# Objekts - Mainīgais no klases
objekts = Nosaukums("Pirmais objekts")
print(objekts.mainigais)
print(objekts.mainigais_2)

# Vērtību uzstādīšana
objekts.mainigais = "Var uzstādīt vērtību"
print(objekts.mainigais)
# objekts.setMainigais("") # Kļūda no 29 rindas
objekts.setMainigais("Uzstāda vērtību izmantojot setter funkc")
print(objekts.mainigais)

# __str__ funkcija
print(objekts)
objekts2 = Nosaukums()
print(objekts2.mainigais_2)
print(objekts2)

# Klases izveide (no 12_nodarbiba.drawio)
# 1. Klases nosaukums
class Bibliotēka:
    # 2. Klases mainīgie
    nosaukums: str
    grāmatas: list[str]
    vaiAtvērta: bool = False

    # 3. init funkcija
    def __init__(self, nosaukums):
        self.grāmatas = []
        self.nosaukums = nosaukums
    
    # 4. citas funkcijas
    def pievienotGrāmatu(self, grāmatas_nosaukums :str):
        self.grāmatas.append(grāmatas_nosaukums)
    def izņemtGrāmatu(self, grāmatas_idx :int):
        self.grāmatas.pop(grāmatas_idx)
    def sāktDarbu(self):
        self.vaiAtvērta = True
    def beigtDarbu(self):
        self.vaiAtvērta = False
    
    def __str__(self):
        return f"Bibliotēka {self.nosaukums}, pašlaik ir {"atvērta" if self.vaiAtvērta else "aizvērta"}, un bibliotēkā ir {len(self.grāmatas)} grāmatas"

# 5. klases pielietošana (obj. izveide)
bibliotēka_1 = Bibliotēka("Pirmā bibliotēka")
bibliotēka_1.pievienotGrāmatu("Nāves Ēnā")
bibliotēka_1.pievienotGrāmatu("The Silmarillion")

bibliotēka_2 = Bibliotēka("Otrā bibliotēka")
bibliotēka_2.sāktDarbu()
print(bibliotēka_1)
print(bibliotēka_2)
print(bibliotēka_2.__dict__)

# Uzdevums: Izveidot klasi no diagrammas (13_nodarbiba.drawio) =>
