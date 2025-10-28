import sys

# Récupérer les arguments à partir de la ligne de commande

argument = sys.argv[1:]

# Vérifier si aucun argument n'a été fourni
if len(argument) == 0:
    print("Vous n'avez rien mis")

# Vérifier si trop d'arguments sont fournis
elif len(argument) > 1:
    print("Tu as besoin que d'une chaine")

# Vérifier si l'argument est un nombre
elif argument[0].isnumeric():
    print("Les chiffres ne sont pas pris en compte")

else:
    # Créer une liste vide
    table = []

    # Parcourir chaque lettre de la chaine
    for letter in argument[0]:
        table.append(letter)

    # Afficher l'index de dernier caractère + 1
    print(len(table))