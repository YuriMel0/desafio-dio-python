menu = """
    OPERAÇÔES
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair

==>"""

saldo = 0
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Informe o valor: "))
        if valor_deposito > 0:
            saldo = valor_deposito
            extrato += f"Deposito R$: {valor_deposito:.2f}\n"
        else:
            print("[ERRO] Valor invalido!")
    elif opcao == "s":
        valor_saque = float(input("informe o valor:"))
        if LIMITES_SAQUES > 0 and valor_saque <= 500:
            saldo -= valor_saque
            LIMITES_SAQUES -= 1
            extrato += f"Valor saque R$: {valor_saque:.2f}\n"
        else:
            print("[ERRO] O valor excede o limmite por saque!") if valor_saque > 500 else print("[ERRO] Quantidade de saque excedido")
    elif opcao == "e":
        print("EXTRATO")
        print(extrato)
    elif opcao == "q":
        break
    else:
        print("desenvolver exeção")
