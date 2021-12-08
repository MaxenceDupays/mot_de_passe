# Générateur de mot de passe.

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/_-"

all = lower + upper + numbers + symbols

longueur = 16

mot_de_passe = "".join(random.sample(all,longueur))
print(mot_de_passe)


