# Saistītas klases
# 1. - Klases kas satur citas klases objektus
class Filma:
    nosaukums: str
    žanrs :str
class Kinoteātris:
    nosaukums: str
    filma: Filma # Klase var tikt lietota kā mainīgā tips
    def __init__(self):
        # mainīgajiem ar klašu datu tipu standarta vērtības
        # jādefinē zem __init__!!!
        self.filma = Filma()
        pass

# Uzdevums:
# Uzrakstīt klasi "Lampa", kas apraksta lampu, un spuldzi tajā.
# Lampas objektam vajadzētu uzglabāt informāciju par lampas stāvokli, un spuldzi tajā.
# Klasei lampa vajag funkciju ieslēgt, kas uzstāda spuldzes ieslēgšanas
# stāvokli. 
# Izveidot objektu & izsaukt lampas ieslēgšanas funkciju & jāizvada spuldzes stāvoklis
class Spuldze:
    modelis :str
    ieslēgta :bool
    def __init__(self, modelis):
        self.modelis = modelis
        self.ieslēgta = False
class Lampa:
    modelis :str
    spuldze: Spuldze
    def __init__(self, modelis, spuldze):
        self.modelis = modelis
        self.spuldze = spuldze
    def ieslēgt(self):
        self.spuldze.ieslēgta = True
lampa = Lampa("AAA", Spuldze("BBB"))
lampa.ieslēgt()
print(lampa.spuldze.ieslēgta)
spuldz =  Spuldze("CCC")
lampa_2 = Lampa("AAA", spuldz)
print(lampa_2.spuldze.ieslēgta)

# Mantošana
# Piemēram transportlīdzekļi => Automašīna, Autobuss, Vilciens...
# Abstrakta klase - netiks izmantota reālu objektu veidošanai
class Transportlīdzeklis:
    ražotājs: str
    modelis: str
    pārvadājamo_skaits :int
    ātrums: float
    riteņu_skaits: int
    def __init__(self, ražotājs, modelis):
        self.ražotājs = ražotājs
        self.modelis = modelis
        self.riteņu_skaits = 0
        self.ātrums = 0.0
        self.pārvadājamo_skaits = 0
    def braukt(self):
        print("Abstrakta klase nevar braukt!")
# Apakšklases - praktiskas klases no kuras veidosim objektus
# Klase no kuras manto tiek norādīta iekavās aiz klases nosaukuma
# Var būt neierobežots skaits klašu no kurām manto
class Automašīna(Transportlīdzeklis):
    def __init__(self, ražotājs, modelis, pārvadājamo_skaits):
        # super() - ļauj izsaukt funkcijas no virsklases
        super().__init__(ražotājs, modelis)
        self.riteņu_skaits = 4
        self.pārvadājamo_skaits = pārvadājamo_skaits
    def braukt(self):
        #super().braukt()
        print("wroom wroom")
class Lidmašīna(Transportlīdzeklis):
    def __init__(self, ražotājs, modelis, pārvadājamo_skaits, dzinēju_skaits, spārnu_platums):
        super().__init__(ražotājs, modelis)
        self.riteņu_skaits = 2
        self.pārvadājamo_skaits = pārvadājamo_skaits
        self.dzinēju_skaits = dzinēju_skaits
        self.spārnu_platums = spārnu_platums
    def braukt(self):
        print("Tikai nosēžoties vai paceļoties!")
    def lidot(self):
        print("woosh!")

auto_1 = Automašīna("BMW", "iX", 5)
lidm_1 = Lidmašīna("Airbus", "A300", 250, 2, 45.0)
lidm_1.lidot()
print(lidm_1.pārvadājamo_skaits)
auto_1.braukt()
print(auto_1.pārvadājamo_skaits)

#Uzdevums:
#* Izveidot grafiku un abstrakta klasi "dzīvnieks". Parametrs - vārds, kāju skaits. Funkcija - skaņa (neko neizvada).
#* Izveidot grafiku un apakšklasi "suns". Funkcija skaņa (izvada "Rej").
#* Izveidot grafiku un apakšklasi "kaķis". Funkcija skaņa (izvada "Ņaud")
# Izveidot objektus sunim un kaķim - izsaukt skaņas funkciju
class Dzīvnieks:
    vārds :str
    kājuSk :int
    def __init__(self, vārds):
        self.kājuSk = 0
        self.vārds = vārds
    def skaņa(self):
        print("Abstrakta klase - nav skaņas")
class Suns(Dzīvnieks):
    def __init__(self, vārds):
        super().__init__(vārds)
        self.kājuSk = 4
    def skaņa(self):
        print("Woof!")
class Kaķis(Dzīvnieks):
    def __init__(self, vārds):
        super().__init__(vārds)
        self.kājuSk = 4
    def skaņa(self):
        print("Meow!")
s1 = Suns("AAA")
s1.skaņa()
s2 = Kaķis("AAA")
s2.skaņa()