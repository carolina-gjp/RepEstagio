import json

with open('faturamento.json', 'r') as file:
    faturamentos = [dia['valor'] for dia in json.load(file) if dia['valor'] > 0]

menor = min(faturamentos)
maior = max(faturamentos)
media = sum(faturamentos) / len(faturamentos)

diasmedia = sum(valor > media for valor in faturamentos)

print('Menor faturamento: R${}' .format(menor))
print('Maior faturamento: R${}' .format(maior))
print('Dias acima da média: {}' .format(diasmedia))
