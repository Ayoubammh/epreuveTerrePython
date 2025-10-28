import sys

argument = sys.argv[1:]

for element in argument:
    try:
        float(element)
    except ValueError:
        print("erreur.")
        sys.exit()

# Verifier qu'il ya au moin deux arguments
if len(argument) <= 1:
    print("Veuillez mettre au minimum 2 argument!")
    sys.exit()

# Vérifier si la liste est triée
for i in range(1, len(argument)):
    if float(argument[i]) < float(argument[i - 1]):
        print("Pas triéé")
        sys.exit()

print("Triée!")