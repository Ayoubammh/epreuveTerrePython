import sys

# Récupérer l'argument passé au script
if len(sys.argv) < 2:
    print("Erreur.")
    sys.exit()

reversed_string = sys.argv[1]
reverse = ""

# Vérifier si l'argument est un nombre ou vide
if reversed_string.isnumeric() or reversed_string == "undefined":
    print("Erreur.")
else:
    # Inverser la chaine
    reverse = reversed_string[::-1]
    print(reverse)