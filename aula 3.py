# se eu tenho uma lista e quero que todos fiquem com a primeira letra maiúscula
lista_nomes = ["Thiago", "João", "pedro", "maria"]

for nome in lista_nomes:
    print(nome.capitalize()),
    
print("\n")

# Exemplo de uma lista de valores quando quero aplicar manipulações
valores= [29.90, 100.00, 150.00]
count = 0
print(valores)

#executa enquanto o número de elementos da lista for maior que zero, no caso 3
while len(valores) > count:
    valores[count] = round(valores[count] * 1.10, 2)
    count = count + 1

print(valores)

#outra opção
for index, valor in enumerate(valores):
    valores[index] = round(valores[index] * 1.10, 2)   
print(valores)
