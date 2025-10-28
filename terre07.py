import sys

# Recupérer les arguments 
arguments = sys.argv[1:]

# Vérifier si aucun argument n'a été fourni
if len(arguments) == 0:
    print("Vous n'avez rien mis")

# Vérifier s'il ya plus d'un argument
elif len(arguments) > 1:
    print("Tu as besoin que d'une chaine")

# Vérifier si l'argument est un nombre
elif arguments[0].isnumeric():
    print("Les chiffres ne sont pas pris en compte")

else:
    table = []

    # Parcourir la chaine et stocker les indices
    for index, letter in enumerate(arguments[0]):
        table.append(index)

    # Afficher le dernier index + 1
    if table:
        print(int(table[-1] + 1))
    else:
        print(0)