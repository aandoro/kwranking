from collections import OrderedDict

sentence = input('Ingrese una oracion: ');

print(" ".join(OrderedDict.fromkeys(sorted(sentence.upper().split()))));