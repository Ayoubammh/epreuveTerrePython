import sys

argument = sys.argv[1:]

# Vérifier le nombre d'arguments
if len(argument) != 3:
    print("Mettez 3 nombres svp.")
    sys.exit()

# Essayer de convertir en entiers (gère les nombres négatifs)
try:
    first_integer = int(argument[0])
    second_integer = int(argument[1])
    third_integer = int(argument[2])
except ValueError:
    print("Met que des chiffres !")
    sys.exit()

# Vérifier si deux nombres sont identiques
if first_integer == second_integer or second_integer == third_integer or third_integer == first_integer:
    print("erreurs.")
    sys.exit()

# Trouver et afficher le nombre médian
sorted_list = sorted([first_integer, second_integer, third_integer])
print(sorted_list[1])
