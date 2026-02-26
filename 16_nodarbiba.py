# Uzdevums:
# Izveidot grafikus un klašu definīcijas internetveikala preču grozam. Par precēm satur nosaukumu un cenu, kamēr grozs satur informāciju par precēm un to daudzumu tajā.
# Grozam jārealizē pievienošanas, izņemšanas funkcionalitāti, kā arī groza vērtības aprēķināšanu.
# Izveidot objektus grozam ar 2 precēm, aprēķināt to vērtību (preces un to vērtības var izdomāt).
class Prece:
    nosaukums: str
    cena: float
    def __init__(self, nosaukums, cena):
        self.nosaukums = nosaukums
        self.cena = cena
class Grozs:
    preces: list[Prece]
    def __init__(self):
        self.preces = []
    def pievienot(self, prece :Prece):
        self.preces.append(prece)
    def iznemt(self, prece :Prece):
        self.preces.remove(prece)
    def aprekinatCenu(self):
        vertiba = 0.0
        for prece in self.preces:
            vertiba += prece.cena
        return vertiba

pr1 = Prece("Maize", 1.30)
pr2 = Prece("Piens", 1.30)
gr1 = Grozs()
gr1.preces.append(pr1)
gr1.preces.append(pr1)
gr1.preces.append(pr2)
print(gr1.aprekinatCenu())


# Jāizveido klase "Bankas Konts". 
# * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
# * Izveidojat funkcijas, kas ļauj ieskaitīt vai izņemt naudu no konta
# * Neļaut lietotājam izņemt naudu ja kontā ir zem €50
# Izveidojat apakšklasi "Krājkonts".
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju, 
#   t.i. izveidojat izņemšanas funkciju priekš krājkonta
#   lai tā kopā ar izņemto naudu izņem vēl 10%
#   (t.i. izņemot €100, izņems €110)
# * Neļaut lietotājam izņemt naudu ja kontā ir zem €100
class BankasKonts:
    lidzekli: float
    def __init__(self):
        self.lidzekli = 0.0
    def ieskaitit(self, summa):
        self.lidzekli += summa
    def iznemt(self, summa):
        print("Izsaukta Bankas konta funkcija")
        if self.lidzekli > 50.0:
            self.lidzekli -= summa
        else:
            print("Kļūda: Pārāk maz")
class Krajkonts(BankasKonts):
    def iznemt(self, summa):
        print("Izsaukta krājkonta funkcija")
        if self.lidzekli > 100.0:
            procSum = summa * 1.10
            super().iznemt(procSum)
        else:
            print("Kļūda: Pārāk maz")
kkonts = Krajkonts()
kkonts.ieskaitit(200)
kkonts.iznemt(100)
print(kkonts.lidzekli)

# Izveidot klasi "Akcija", kas glabā informāciju par akcijām
# Nosaukums, & nominālvērtība
class Akcija:
    nosaukums: str
    nominālvērtība: float
    def __init__(self, nosaukums, nominālvērtība):
        self.nosaukums = nosaukums
        self.nominālvērtība = nominālvērtība

# Izveidot klasi AkcijuKonts, kas glabā informāciju par lietotāja naudas
# (mantot no BankasKonts) līdzekļiem un akciju līdzekļiem.
class AkcijuKonts(BankasKonts):
    akcijas: list[Akcija]
    def __init__(self):
        super().__init__()
        self.akcijas = []
    # Realizēt akciju pievienošanas un izņemšanas funkcijas.
    # Izvadot objektu (print(obj)) vajadzētu izvadīt informāciju par lietotāja -- __str__
    # naudas atlikumu, akciju skaitu un to vērtību vērtību.
    def pievienotAkc(self, akcija):
        self.akcijas.append(akcija)
    def iznemtAkc(self, akcija):
        self.akcijas.remove(akcija)
    def __str__(self):
        vertiba = 0.0
        for iii in self.akcijas:
            vertiba += iii.nominālvērtība
        return f"Līdzekļi: {self.lidzekli}, Akciju skaits: {len(self.akcijas)}, Akc. Vērtība: {vertiba}"
akc = AkcijuKonts()
akc.ieskaitit(200)
akc.pievienotAkc(Akcija("AAA", 100))
otrAkc = Akcija("AAA", 100)
akc.pievienotAkc(otrAkc)
print(akc)