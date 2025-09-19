teksts = "Kaut kas"
print(teksts[5:])
print(len(teksts))

# Uzdevums: Ir dots skaitlis 123456 mainīgajā. 
# Izvadam trešo ciparu (3).
# skaitlis = str(123456)[2]
# print(skaitlis)

saraksts = [ 123, "asd", [ 123, 32, [ 3, 4] ] ]
print(len(saraksts)) # Dzēšana...
saraksts.pop(2)
print(saraksts)

skaitlis = 10
# pārbaude = skaitlis == 11
# print(pārbaude)
#if skaitlis == 11 or skaitlis == 10: # Vai - izpildās, ja izpildās viens nosacījums
#if skaitlis == 11 and skaitlis == 10: # Un - izpildās, ja izpildās abi nosacījumi
if skaitlis == 11: # Ja, tad...
    print("Izpildās")
elif skaitlis == 12: # Ja iepiekšējie neizpildās (Else if), tad...
    print("Šis izpildās...")
else: # Ja neviens neizpildās, tad...
    print("pēdējais variants")
#print("Nav zem if")

# ==, is - Vienāds ar
# != - nav vienāds ar
# not - Pretēja pārbaude
if not skaitlis == 11 and skaitlis != 15:
    print("Skaitlis nav 11 un 15")
# > - lielāks par
# < - mazāks par
# >= - lielāks VAI vienāds
# <= - mazāks VAI vienāds

# Ievade
# ievadītais_teksts = input("Ievade: ")
#print(ievadītais_teksts)
#print("2" + ievadītais_teksts)
# print(2 + float(ievadītais_teksts))

# Uzdevums 1: Izvada lietotāja ievadi
# Ievade: Cilvēka Vārds: 
# Izvade: Sveiks, <Vārds>!
# ievade = input("Cilvēka vārds: ")
# print(f"Sveiks, {ievade}!")
#print("Sveiks,", ievade, "!")

# Uzdevums 2:
# Ievade: Skaitlis
# Izvade: "Jā", ja skaitlis ir lielāks par 10, "Nē" ja ir mazāks
# skaitlis = input("Ievade: ")
# if skaitlis.isnumeric(): # Pārbauda vai ir skaitlis -- alternatīva - .isdigit()
#     skaitlis = int(skaitlis)
#     if skaitlis > 10:
#         print("Jā")
#     else:
#         print("Nē")
# else:
#     print("Nav skaitlis!")

# Uzdevums 3:
# Ievade: Jebkāds teksts
# Izvade: Šī teksta 1, 3 un 5 burts.
# NB. Jāveic pārbaude vai ir tik garš teksts.
ievade = input("Ievade: ")
if len(ievade) >= 5:
    print(f"1: {ievade[0]}, 3: {ievade[2]}, 5: {ievade[4]}")
    #print("1:", ievade[0], "3:", ievade[2], "5:", ievade[4])