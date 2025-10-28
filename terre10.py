import sys

# Récupére les arguments 
argument = sys.argv[1:]

if len(argument) == 0:
    print("Vous devez mettre un nombre.")
    sys.exit()

number_str = argument[0]

#Vérification du type
if not number_str.isdigit():
    print("Vous devez mettre un nombre.")
    sys.exit()

if len(argument) != 1:
    print("Vous devez mettre juste un nombre.")
    sys.exit()

number = int(number_str)

#Cas particuliers
if number == 1:
    print("Le chiffre 1 n'est pas pris en compte.")
    sys.exit()

# Diviser le nombre en chiffre individuels
table_number = [int(chiffre) for chiffre in str(number)]

#Additionner les chiffres pour vérifier divisibilité par 3 ou 9
total_number = sum(table_number)

# Récuperer le dernier chiffre pour tester divisibilité par 2 ou 5
last_digit = number % 10

# Vérification des cas
if number in (2, 3, 5):
    print(f"Oui, {number} est un nombre premier.")

elif last_digit == 0 or last_digit == 5:
    print(f"Non, {number} n'est pas un nombre premier.")

elif last_digit % 2 == 0:
    print(f"Non, {number} n'est pas un nombre premier.")

elif total_number % 3 == 0 or total_number % 9 == 0:
    print(f"Non, {number} n'est pas un nombre premier.")

else:
    print(f"Oui, {number} est un nombre premier.")
