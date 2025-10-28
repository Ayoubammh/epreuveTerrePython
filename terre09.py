import sys

# Récupérer les arguments 
argument = sys.argv[1:]

# Vérifications
if len(argument) == 0:
    print("Vous n'avez rien mis !")

elif not argument[0].isdigit():
    print("Vous devez mettre un nombre !")

elif len(argument) != 1:
    print("Il ne doit y avoir qu'un nombre !")

else:
    number = int(argument[0])
    square_root = 0

    # Trouver la racine carré entière la plus proche
    i = 0
    while i * i <= number:
        square_root = i
        i += 1

    print(square_root)