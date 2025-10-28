import sys

# Récupere les arguments
argument = sys.argv[1:]

# Vérifier si un argument a été donné
if len(argument) == 0:
    print("Rentrer un argument")
    sys.exit()

# Vérifier s'il y a plus d'un argument
if len(argument) != 1:
    print("Un argument stp !")
    sys.exit()

# Récupérer les heures et minutes
heure_str = argument[0]

# Vérifier le format minimal (HH:MM)
if len(heure_str) < 5 or ":" not in heure_str:
    print("Mettez le bon format !")
    sys.exit()

heures = heure_str[:2]
minutes = heure_str[3:5]

# Vérifier que ce sont bien des chiffres
if not (heures.isdigit() and minutes.isdigit()):
    print("Mettez le bon format !")
    sys.exit()

heures = int(heures)
minutes = int(minutes)

# Conditions de validation et conversion
if heures > 24:
    print("Nous n'avons que 24H dans une journée.")
elif minutes >= 60:
    print("Nous n'avons que 60 minutes dans une heure.")
elif heures == 0:
    print(f"12:{minutes:02d}pm")
elif heures > 12:
    print(f"{heures - 12}:{minutes:02d}pm")
elif heures <= 12:
    print(f"{heures:02d}:{minutes:02d}am")
else:
    print("Mettez le bon format !")