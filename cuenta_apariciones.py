from collections import Counter

appearances = {}
text = input('Ingrese una oracion: ')
letter_counts = Counter(text).most_common()

for  (i,l_c) in letter_counts:
    appearances[i] = l_c

for (letter, count) in appearances.items():
    print(letter,':',count)