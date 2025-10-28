import sys 

# Récupérer les arguments 
arguments = sys.argv[1:]

# Récupérer le premier nombre et l'exposant
if len(arguments) >= 1:
    base_number = arguments[0]
else:
    base_number = None

if len(arguments) >= 2:
    exponent = arguments[1]
else:
    exponent = None

# Vérification des erreurs
if base_number is None:
    print("Vous n'avez rien mis !")

elif len(arguments) != 2:
    print("Il ne faut avoir que deux nombres !")

elif exponent is not None and exponent.startswith('-'):
    print("L'exposant doit etre positif !")

# Vérifier si ce sont bien des nombres
elif not (base_number.replace('.', '', 1).isdigit() and exponent.replace('.', '',1).isdigit()):
    print("Vous devez mettre que des nombres !")

else:
    base_number = float(base_number)
    exponent = int(exponent)

    puissance = base_number
    for i in range(1, exponent):
        puissance *= base_number

    print(puissance)