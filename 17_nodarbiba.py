#isbn    title    author    published_year    genre    in_stock    location_shelf
#9780140449136    The Odyssey    Homer    -800    Epic    3    A-12
#9780553386790    A Short History of Nearly…    Bill Bryson    2003    Nonfiction    5    B-07
#9780747532743    Harry Potter and the…    J.K. Rowling    1997    Fantasy    0    R-02
class GramataBiblioteka:
    isbn :int
    title :str
    author :str
    published_year :int
    genre :str
    in_stock :int
    location_shelf :str
    def __init__(self, isbn, author, title, year, genre, stock, location):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.published_year = year
        self.genre = genre
        self.in_stock = stock
        self.location_shelf = location
    # Uzdevums: Pievienot funkc, kas izmaina grāmatu skaitu
    def izmSkaitu(self, skaits):
        self.in_stock = skaits
    def __str__(self):
        return self.title
    
gram1 = GramataBiblioteka(9780140449136, "The Odyssey", "Homer", -800, "Epic", 3, "A-12")
print(gram1)
gram2 = GramataBiblioteka(9780553386790, "A Short History of Nearly…", "Bill Bryson", 2003, "Nonfiction", 5, "B-07")
#...

# Uzdevums: Izveidot klasi - Student, un objektus no sekojošās tabulas
# Izveidot funkciju, kas nomaina studenta skapīša numuru
# Izvadot studentu (print(obj)) jāizvada studenta id un pilns vārds. Izvadīt abus studentus.
#student_id    full_name   is_enrolled    locker_number
#S-1001    Anna Ozoliņa    true    112
#S-1002    Jānis Bērziņš    true   332
class Student:
    student_id :str
    full_name :str
    is_enrolled :bool
    locker_number :int
    def __init__(self, id, name, enrolled, number):
        self.student_id = id
        self.full_name = name
        self.is_enrolled = enrolled
        self.locker_number = number
    def nomSkap(self, nr):
        self.locker_number = nr
    def __str__(self):
        return f"[{self.student_id}] {self.full_name}"
stud = Student("S-1001", "Anna Ozoliņa", True, 112)
print(stud)

# 1. Uzd - 1. daļa
# Izveidot grafiku un klasi kas apraksta darbinieku kādā uzņēmumā. Jāuzglabā informācija par darbinieka vārdu, algu un amatu.
# Jānodefinē funkcijas - aprēķini bonusu (šai klasei funkcija atgriež vērtību 0)
# un algas aprēķins - saskaita algu + bonusa funkcijas rezultātu.
class Darbinieks:
    vards: str
    alga: float
    amats: str
    def __init__(self, vards, alga, amats):
        self.vards = vards
        self.alga = alga
        self.amats = amats
    def aprBonus(self) -> float:
        return 0.0
    def saskAlg(self) -> float:
        return self.alga + self.aprBonus()
# 2. daļa Izveidot apakšklases sekojošiem amatiem - 
# 1. Menedžeris - Glabā informāciju par to, cik darbinieki ir zem menedžera. Bonuss - darbinieku skaits * 100
# 2. Programmētājs - Glabā informāciju par to, pie kāda projekta pašlaik strādā. Bonuss  - 10% no algas
# 3. Testeris - Glabā informāciju par to, pie kāda projekta pašlaik strādā, un cik stundas ir nostrādājis šajā mēnesī. Bonuss - 5% no algas. Kopalgas aprēķinā tiek reizināta algas likme ar stundu skaitu (nevis atgriezta vienkārši alga)
class Menedzeris(Darbinieks):
    darbinieki: int
    def __init__(self, vards, alga, amats, darbinieki):
        super().__init__(vards, alga, amats)
        self.darbinieki = darbinieki
    def aprBonus(self):
        return self.darbinieki * 100
class Programmetajs(Darbinieks):
    projekts :str
    def aprBonus(self):
        return self.alga * 0.1
class Testeris(Darbinieks):
    stundas: float = 0.0
    def aprBonus(self):
        return self.alga * 0.05
    def saskAlg(self):
        return (self.alga * self.stundas) + self.aprBonus()