import sys

# Récupérer l'argument
if len(sys.argv) < 2:
    print("Tu ne me la mettras pas à l'envers.")
    sys.exit()

try:
    number_parity = int(sys.argv[1])
except ValueError:
    print("Tu ne me la mettras pas à l'envers.")
    sys.exit()

# Vérifier la parité
if number_parity % 2 == 0:
    print("pair")
else:
    print("impair")