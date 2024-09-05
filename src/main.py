menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

==>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("desenvolver deposito")
    elif opcao == "s":
        print("desenvolver saque")
    elif opcao == "e":
        print("desenvolver Extrato")
    elif opcao == "q":
        break
    else:
        print("desenvolver exeção")
