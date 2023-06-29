# Deposito, saque e extrato


deposit_list = []
LIMITE_SAQUES = 3
limite_valor = 500

deposit_value = input("Qual o valor deseja depositar? ")
if int(deposit_value) < 0:
    print("Erro ao depositar: Valor inválido!")
else:
    deposit_list.append(deposit_value)
    print(f"valor de R${deposit_value} depositado!")

while True:
    opcao = input("Informe uma ")
