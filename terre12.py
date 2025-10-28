import sys

argument = sys.argv[1:]

# Vérifications
if len(argument) != 1:
    print("Met un argument stp!")
    sys.exit()

time_str = argument[0]

# Extraire les heures, minutes et le suffixe AM/PM
heures = time_str[:2]
minutes = time_str[3:5]
time_table = time_str[5:7]

# Vérifier que le format de base est correct
if not (heures.isdigit() and minutes.isdigit()):
    print("Mettez le bon format !")
    sys.exit()

heures = int(heures)
minutes = int(minutes)

#Vérifications des limites
if heures > 24:
    print("Nous n'avons que 24H dans une journée.")
elif minutes >= 60:
    print("Nous n'avons que 60 minutes dans une heure.")
elif time_str == f"12:{minutes:02d}PM":
    print(time_str[:5])
elif time_table == "PM":
    print(f"{heures + 12}{time_str[2:5]}")
else:
    print("Mettez le bon format !")