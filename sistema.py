import os
import time
import datetime
extrato = ""
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10

menu = """
0 - Depositar | 1 - Sacar | 2 - Consultar Extrato | 3 - Sair

"""
print(
     """
Seja bem-vindo ao banco Codea! 
      
Qual operação você desesja realizar hoje?
      """
      )      
while True:
    print(menu)
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número.")
        continue

    os.system("cls")
    
    # Depósito
    if opcao == 0:
        valor = float(input("Digite a quantia que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"+ R$ {valor:.2f}\n"
            print(f"Seu depósito de R$ {valor} foi realizado com sucesso.")
            print(f"Saldo após depósito: {saldo}")
        
        else:
            print("Por favor, digite um valor válido para depositar.")

    # Saque
    elif opcao == 1:
        valor = float(input("Digite a quantia que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
                print("Você não tem saldo o suficiente para realizar um saque desse valor.")
                time.sleep(2)
                os.system("cls")
        elif excedeu_limite:
                print("O limite de saque é de R$500.00")
                time.sleep(2)
                os.system("cls")
        elif excedeu_saques:
                print("Você atingiu o limite diário de saques. Tente novamente amanhã.")
                time.sleep(2)
                os.system("cls")
        else:
            print(f"Seu saque de R$ {valor} foi realizado.")
            saldo -= valor
            extrato += f"- R${valor:.2f}\n"
            print(f"Saldo após saque: R$ {saldo}")

    # Extrato        
    elif opcao == 2:
        print("Não existem movimentações recentes." if not extrato else extrato)
        print(f"\nSaldo: {saldo:.2f}, {datetime.now()}")


    elif opcao == 3:
        print("Obrigado por usar o banco Codea. Volte sempre!")
        time.sleep(2)
        break

    else:
        print("Operação inválida, por favor, digite novamente a operação desejada.")
        time.sleep(2)
        os.system("cls")


        