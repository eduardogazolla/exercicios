def inverter_string(string):
    caracteres = list(string)

    inicio = 0
    fim = len(caracteres) - 1

    while inicio < fim:
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        inicio += 1
        fim -= 1
    return ''.join(caracteres)

string_original = "Hello, world!"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
