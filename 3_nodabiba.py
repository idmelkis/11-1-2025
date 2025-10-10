# Uzdevums: Kalkulators
# Ievade: Divi skaitļi, darbība 
# (saskaitīšana, atņemšana, dalīšana un reizināšana)
# (+, -, /, *)
# Izvade: Noteiktās darbības rezultāts
# skaitlis1 = float(input("Skaitlis 1: ")) # int - skaitlis, float - daļskaitlis
# skaitlis2 = float(input("Skaitlis 2: ")) 
# darbiba = input("Darbība: ")
# if darbiba == "+":
#     print(skaitlis1+skaitlis2)
# elif darbiba == "-":
#     print(skaitlis1-skaitlis2)
# elif darbiba == "/":
#     print(skaitlis1/skaitlis2)
# elif darbiba == "*":
#     print(skaitlis1*skaitlis2)
# else:
#     print("Nezināma darbība")

# switch / python - match
# match darbiba:
#     case "+":
#         print(skaitlis1+skaitlis2)
#     case "-":
#         print(skaitlis1-skaitlis2)
#     case "/":
#         print(skaitlis1/skaitlis2)
#     case "*":
#         print(skaitlis1*skaitlis2)
#     case _:
#         print("Nezināma darbība")

# Cikli
# While, For
#while <darbība kas izpildās uz True>:
#while True: # Cikls kas izpildīsies līdz viņu manuāli pārtrauc
# pārbaude = 1 == 2
# print(pārbaude)
# while pārbaude:
#     print("Strādā")
# tests = 0
# while tests <= 10:
#     tests += 1
#     if tests == 2:
#         continue # Pārtrauc iterāciju, turpina nākošo
#     if tests == 4:
#         break # Pārtrauc ciklu
#     print(tests)

# saraksts = [ 0, "tests", 3]
# for mainīgais in saraksts:
#     print(mainīgais)

# saraksts = [ 0, 1, 2 ... ]
# for skaitlis in range(0, 11, 2): # sākot no 0, līdz 10, izvadam katru 2 sk.
#     print(skaitlis)

# skaitītājs = 0
# while skaitītājs < 11:
#     print(skaitītājs)
#     skaitītājs += 2

# Uzdevums - Dots saraksts
# saraksts = [ 0, 2, 4, 5, 9]
# Uzrakstat ciklu (brīvas izvēles), kurš izvada saraksta vērtības * 2.
# for skaitlis in saraksts:
#     print(skaitlis * 2)

# Uzdevums: Dots for cikls, kas izvada trešo saraksta vērtību
# Uzrakstīt šo ciklu while formā
saraksts = [1, 5, 7, 4, 3, 9]
for idx in range(len(saraksts)): # Range no 0 līdz saraksta garumam - piem., ja garums ir 4, tad idx būs 0,1,2,3
    if saraksts[idx] == 3:
        print(idx)
        break
idx = 0
while idx < len(saraksts):
    if saraksts[idx] == 3:
        print(idx)
        break
    idx += 1