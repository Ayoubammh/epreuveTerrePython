import sys
import re

# Récupérer les arguments (on ignore les deux premiers si besoin)
args = sys.argv[2:] if len(sys.argv) > 2 else sys.argv[1:]

# Vérifier qu'on a bien une seule lettre
if len(args) != 1 or not re.match(r"^[a-zA-Z]$", args[0]):
    print("Error")
    sys.exit()

# Récupérer la lettre
letter = args[0]
ascii_number = ord(letter)

# Définir la limite ('z' = 122)
last_letter = 123
result = ""

# Construire la séquence
for i in range(ascii_number, last_letter):
    result += chr(i)

print(result)
