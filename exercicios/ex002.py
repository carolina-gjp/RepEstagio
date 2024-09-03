numero = int(input('Informe um número para verificar se pertence a sequência de Fibonacci:'))

a = 0
b = 1

if numero == a or numero == b:
    print('O número {} pertence à sequência de Fibonacci.' .format(numero))
else:
    
    while b < numero:
        a, b = b, a + b
    if b == numero:
        print('O número {} pertence à sequência de Fibonacci.' .format(numero))
    else:
        print('O número {} não pertence à sequência de Fibonacci.' .format(numero))