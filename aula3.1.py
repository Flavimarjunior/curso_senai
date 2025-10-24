lista_clientes = [
    ["nome", "endereço", "telefone", "saldo"],
    ["thiago", "av 123", "(19) 99999-9999", "R$40,00"],
    ["lucas", "av 1234", "(19) 88888-8888", "R$30,00"]
]

#vai pegar cada um dos registros e colocar na variável, se eu passar o índice eu pego a coluna
#Fatiamento de listas, ***ESTUDAR
#for clientes in lista_clientes[1:]:
   # print(clientes[0].capitalize())
    # print(clientes[3].replace("R$", "").replace(",", "."))

for item in lista_clientes[1:]:
    soma = float(item[3].replace("R$","").replace(",","."))
    print(soma)
    
# Atualiza os saldos
for saldo in range(1, len(lista_clientes)):
    saldo_float = float(lista_clientes[saldo][3].replace("R$", "").replace(",", "."))
    lista_clientes[saldo][3] = saldo_float

# Imprime a tabela atualizada
for linha in lista_clientes:
    print(linha)

#***Estudar Método de String

