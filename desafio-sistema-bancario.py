menu = """
|============================|
|       Seja bem-vindo       |
|============================|
|Informe a operação desejada:|
|============================|
|   [d] Depositar            |
|   [s] Sacar                |
|   [e] Extrato              |
|   [q] Sair                 |
|============================|
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
saque = 0
deposito = 0
while True:
    opcao = input(menu)
    if opcao.lower().strip() == "d":
        print("|"+"".center(28,"=")+"|")
        print("|"+f"Saldo atual é R${saldo:.2f}".center(28)+"|")
        print("|"+"Depósito selecionado".center(28)+"|")
        print("|"+"".center(28,"=")+"|")
        deposito = float(input("|"+"Digite o valor do depósito: ".center(28)+"| "))
        if deposito > 0:
            saldo += deposito
            extrato += (f"+R${deposito:.2f}".center(30)+"\n") 
            print("|"+"".center(28,"=")+"|")
            print("|"+f"Seu novo saldo é R${saldo:.2f}".center(28)+"|")
            print("|"+"".center(28,"=")+"|")
        else:
            print("|"+"".center(28,"=")+"|")
            print("|"+"Valor inválido".center(28)+"|")
            print("|"+"Depósito não realizado".center(28)+"|")
            print("|"+"".center(28,"=")+"|")
    elif opcao.lower().strip() == "s":
        if numero_saques != LIMITE_SAQUES and saldo > 0:
            print("|"+f"Saldo atual é R${saldo:.2f}".center(28)+"|")
            print("|"+"Saque selecionado".center(28)+"|")
            print("|"+"".center(28,"=")+"|")
            saque = float(input("|"+"Digite o valor do saque: ".center(28)+"| "))
            if saque <= 500 and saque > 0 and saque <= saldo:
                saldo -= saque
                numero_saques += 1
                extrato += (f"-R${saque:.2f}".center(30)+"\n")
                print("|"+f"Seu novo saldo é {saldo:.2f}".center(28)+"|")
                print("|"+"".center(28,"=")+"|")
            elif saque <= 0:
                print("|"+"Valor inválido".center(28)+"|")
                print("|"+"".center(28,"=")+"|")
            elif saque > saldo:
                print("|"+"Você não pode sacar".center(28)+"|") 
                print("|"+"um valor maior que o saldo".center(28)+"|")
                print("|"+"".center(28,"=")+"|")
            else:
                print("|"+"O limite de saque é de".center(28)+"|") 
                print("|"+"R$500,00 por saque".center(28)+"|")
                print("|"+"".center(28,"=")+"|")
        elif numero_saques != LIMITE_SAQUES and saldo == 0:
            print("|"+"".center(28,"=")+"|")
            print("|"+"Você não possui".center(28)+"|")
            print("|"+"saldo para sacar".center(28)+"|")
            print("|"+"".center(28,"=")+"|")
        else:
            print("|"+"Limite de saques atingidos".center(28)+"|")
    elif opcao.lower().strip() == "e":
        print("|"+"".center(28,"=")+"|")
        if extrato != "":
            print("|"+"Extrato".center(28)+"|")
            print("|"+"".center(28,"=")+"|")
            print("")
            print(extrato)
            print("|"+"".center(28,"=")+"|")
            print("|"+f" Saldo atual R${saldo:.2f}".center(28)+"|")
        else:
            print("|"+"Extrato".center(28)+"|")
            print("|"+"".center(28,"=")+"|")
            print("|"+"Zero operações realizada".center(28)+"|")
        print("|"+"".center(28,"=")+"|")
    elif opcao.lower().strip() == "q":
        break
    else:
        print("|"+"".center(28,"=")+"|")
        print("|"+"Operação inválida,".center(28)+"|")
        print("|"+"por favor selecione".center(28)+"|" )
        print("|"+"novamente a".center(28)+"|") 
        print("|"+"operação desejada".center(28)+"|")
        print("|"+"".center(28,"=")+"|")

#desafio sistema bancário dio
#https://github.com/renan1221
