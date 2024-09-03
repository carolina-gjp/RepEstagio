entrada = input('Digite uma string para inverter:')

resultado = ''

for i in range(len(entrada) - 1, -1, -1):
    resultado += entrada[i]

print('String invertida:', resultado)