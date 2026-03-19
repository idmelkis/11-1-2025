# Faili: https://en.wikipedia.org/wiki/Computer_file
# Diska sektori: https://en.wikipedia.org/wiki/Disk_sector
# Failu sistēma kuru lieto Windows: https://en.wikipedia.org/wiki/NTFS

#mainīgais = "vērtība"

# Dokumentācija: https://docs.python.org/3/library/os.html
import os
# Absolūtais ceļš:
# Windows: "C:\Users\idmelkis\Downloads\ASDASDA.docx"
# Linux: "/var/log/file.log"

# Relatīvais ceļš:
# Papildus informācija: https://www.lenovo.com/au/en/glossary/relative-path/
print(os.getcwd())
# Fails uz desktopa - strādājām mapē "11-1-2025" kas atrodas uz desktop
# .\\ = pašreizējā mape
# ..\\ = iepriekšējā mape
# ..\\.. = Mape virs iepriekšējās mapes
# var miksēt
# Iekš python jālieto divas slīpsvītras, jo viena slīpsvītra tiek izmantota arī speciāliem simboliem, piem \n (jauna rinda)
print(os.path.isfile(".\\19_nodarbiba.py"))
print(os.path.isfile(".\\..\\mape\\..\\11-prog3.txt"))
print(os.path.isfile("C:\\Users\\idmelkis\\Downloads\\..\\Desktop\\11-prog3.txt"))

# os.path.isfile - pārbauda vai eksistē FAILS
# os.path.isdir - pārbauda vai eksistē MAPE
# os.path.exists - pārbauda vai eksistē CEĻŠ
print(os.path.isdir("C:\\Users\\idmelkis\\Downloads\\"))
print(os.path.isdir("..\\mape"))
print(os.path.exists("C:\\Users\\idmelkis\\Downloads\\"))
print(os.path.exists("C:\\Users\\idmelkis\\Downloads\\ASDASDA.docx"))
print(os.path.exists("C:\\Users\\idmelkis\\EEE"))

# Nomainam pašreizējo programmas darbību uz jūsu py faila atrašanās vietu
pašreizējais_fails = __file__
print(pašreizējais_fails)
faila_mape = os.path.dirname(pašreizējais_fails)
print(faila_mape)
# Fails uz desktop
print(os.path.isfile(f"{faila_mape}\\..\\11-prog3.txt"))
# Mainam mapi kurā strādā programma
os.chdir(faila_mape)
print(os.getcwd())

# Copy-paste variants lai nomainītu mapi
os.chdir(os.path.dirname(__file__))

# Alternatīvs veids kā iegūt python faila atrašanās vietu
# Tas strādā, jo palaižot python programmas, viņas tiek palaistas kā `python <jūsu .py fails>`
# Labs veids kā iegūt tieši .py faila nosaukumu - nevajadzētu uzticēties pilna ceļa iegūšanai, jo ne vienmēr argv0 būs pilns ceļš.
# argv[1] u.tt. ir parametri kas tiek padoti programmai, piem. iekš komandrindas
# piem palaižot `python 19_nodarbiba.py --help` iekš sys.argv[1] atrastos teksts `--help`. Šādi var norādīt vairākus parametrus (atdalot ar atstarpi).
import sys
print(sys.argv[0])
#print(sys.argv[1])

# N.B. Neglabājam failus uz servera & failos/mapēs neliekam atstarpes!!!
# Nākošajā stundā - failu izveide, rakstīšana, atvēršana u.t.t.