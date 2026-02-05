# Uzdevums: Izveidot klašu diagrammu automašīnai (fails ar .drawio paplaš.)
# Jārealizē automašīnas braukšanas stāvoklis (ieslēgts, ātrums),
# kā arī paātrinājuma un bremzēšanas funkcionalitāte.
#
# Pēc tam - izveidot klases definīciju (iekš .py faila), izveidot objektu un izsaukt mašīnas ieslēgšanas funkciju
class Automašīna:
    modelis :str
    brends :str
    ieslegta :bool = False
    atrums :float = 0.0
    def __init__(self, modelis, brends):
        self.modelis = modelis
        self.brends = brends
    def ieslegt(self):
        if self.ieslegta == True:
            print("Mašīna jau ir ieslēgta!")
        else:
            self.ieslegta = True
    def izslegt(self):
        if self.ieslegta == False:
            print("Mašīna jau ir izslēgta!")
        else:
            self.ieslegta = False
    def paatrinat(self, atrums):
        self.atrums += atrums
    def bremzet(self, atrums):
        self.atrums -= atrums
masina = Automašīna("Corolla", "Toyota")
masina.ieslegt()

#Uzdevums: Izveidot klašu diagrammu un klases definīciju bezvadu austiņām.
#Klasei jābūt identificējošai informācijai (modelis, brends utt.), savienošanās stāvoklis, skaļuma līmenis. Jārealizē pievienošanās, atslēgšanās, skaņas līmeņa izmaiņas un dziesmas spēlēšanas funkcionalitāte
#Izveidot objektu - palaist savienošanās, skaņas līmeņa palielināšanas un dziesmas spēlēšanas funkcijas, jāizvada informācija par austiņām (__str__).
class Austinas:
    modelis :str
    brends :str
    savienots :bool = False
    skalums :float = 0.0
    dziesmas_statuss :str = ""

    def __init__(self, modelis, skalums):
        self.modelis = modelis
        self.skalums = skalums
    def pieslegties(self):
        # Uzlabot: sekot kādai ierīcei ir pieslēdzies
        self.savienots = True
    def atslegties(self):
        # Uzlabot: sekot kādai ierīcei ir pieslēdzies
        self.savienots = False
    def palielinat_skalumu(self):
        # Var padot arī kā parametru - vai vienkārši palielināt par noteiktu %
        self.skalums += 5
    def samazinat_skalumu(self):
        if self.skalums > 0: # Skaļums nevar būt negatīvs!
            self.skalums -= 5
    def spelet_dziesmu(self, dziesma):
        # Uzlabot: sekot līdzi dziesmas statusam
        print(f"Spēlē {dziesma}")
        self.dziesmas_statuss = dziesma
    def __str__(self):
        return f"{self.brends} {self.modelis} - Skaļums {self.skalums} - {self.dziesmas_statuss if len(self.dziesmas_statuss) > 0 else ''}"


#Izveidot objektu - palaist savienošanās, skaņas līmeņa palielināšanas un dziesmas spēlēšanas funkcijas, jāizvada informācija par austiņām (__str__).
obj = Austinas("???", "???")
obj.savienots()
obj.palielinat_skalumu()
print(obj)