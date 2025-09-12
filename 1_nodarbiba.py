# Komentāri
# Automātiski aizkomentēt - CTRL + K -> CTRL + C
# VAI CTRL + /
print("Teksts")
# int, float, str, boolean
skaitlis = 100 # int
dalskaitlis = 10.5 # float / double
teksts = "teksts"
patiesa_vertiba = True # vai False, boolean 
print(10 == int("10")) # Teksts pārveidots par skaitli
print(str(10)) # Pārveido skaitli par tekstu
print(10) # Print automātiski veic šo pārveidošanu
print(skaitlis)

# Vairāku mainīgo izvade ar print
print("Teksts: ", skaitlis, dalskaitlis) # 1. var - komats
print("Teksts: " + str(skaitlis) + str(dalskaitlis)) # 2. var - +
print(f"Teksts: {skaitlis} {dalskaitlis}") # 3. var - fmt str

"""
Komentārs
Vairākās
Rindās
"""

saraksts = [ 123, "asd", [ 123, 32 ] ] # jeb masīvs - glabā vairākas vērtības vienā mainīgajā
# sda = (123, 234) # Tuple
# asd = {} # Vārdnīca
print(saraksts[2][0]) # Otrā idx vērtības 0 idx vērtība
print(saraksts[1:]) # Pēdējās 2 vērtības
print(saraksts[:2]) # Pēdējās 2 vērtības
saraksts[0] = 333
print(saraksts)
saraksts.append("Pievienota galā")
print(saraksts)
saraksts.insert(0, "Pievienots sākumā")
print(saraksts)
# Dzēšana...