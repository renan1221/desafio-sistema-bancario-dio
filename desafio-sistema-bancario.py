import textwrap
def menu():
    menu = """
|============================|
|       Seja bem-vindo       |
|============================|
|Informe a operação desejada:|
|============================|
|   [D] Depositar            |
|   [S] Sacar                |
|   [E] Extrato              |
|   [C] Nova Conta           |
|   [L] Listar Contas        |
|   [U] Novo Usuário         |
|   [Q] Sair                 |
|============================|
"""
    return input(textwrap.dedent(menu))

def linha():
    print("|"+"".center(28,"=")+"|")
    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += (f"\nDepósito: R$ {valor:.2f}".center(28))
        linha()
        print("|"+"Depósito realizado".center(28)+"|") 
        print("|"+"com sucesso!".center(28)+"|")
        linha()
    else:
        linha()
        print("|"+"Operação falhou!".center(28)+"|")
        print("|"+"O valor informado".center(28)+"|") 
        print("|"+"é inválido".center(28)+"|")
        linha()

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        linha()
        print("|"+"Operação falhou!".center(28)+"|")
        print("|"+"Você não tem".center(28)+"|") 
        print("|"+"saldo suficiente".center(28)+"|")
        linha()

    elif excedeu_limite:
        linha()
        print("|"+"Operação não realizada!".center(28)+"|")
        print("|"+"O valor do saque".center(28)+"|") 
        print("|"+"excede o limite".center(28)+"|")
        linha()

    elif excedeu_saques:
        linha()
        print("|"+"Operação falhou!".center(28)+"|")
        print("|"+"Número máximo".center(28)+"|") 
        print("|"+"de saques excedido".center(28)+"|")
        linha()

    elif valor > 0:
        saldo -= valor
        extrato += (f"\nSaque: R$ {valor:.2f}".center(28))
        numero_saques += 1
        linha()
        print("|"+"Saque realizado".center(28)+"|")
        print("|"+"com sucesso!".center(28)+"|")
        linha()

    else:
        linha()
        print("|"+"Operação fracassada".center(28)+"|") 
        print("|"+"O valor inválido".center(28)+"|")
        linha()

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    linha()
    print("|"+"Extrato".center(28)+"|")
    linha()
    print("""|          Não foram         | 
|  realizadas movimentações  |""" if not extrato else extrato)
    linha()
    saldoo = f"Saldo: R$ {saldo:.2f}"
    print(f"{saldoo}".center(28))
    linha()

def criar_usuario(usuarios):
    linha()
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        linha()
        print("|"+"Já existe usuário".center(28)+"|") 
        print("|"+"com esse CPF!".center(28)+"|")
        linha()
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    linha()
    print("|"+"Usuário criado".center(28)+"|") 
    print("|"+"com sucesso!".center(28)+"|")
    linha()

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    linha()
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        linha()
        print("|"+"Conta criada com sucesso!".center(28)+"|")
        linha()
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    linha()
    print("|"+"Usuário não encontrado".center(28)+"|")
    print("|"+"fluxo de criação de".center(28)+"|") 
    print("|"+"conta encerrado!".center(28)+"|")
    linha()

def listar_contas(contas):
    for conta in contas:
        linhaa = f"""\
               Agência:\t{conta['agencia']}
               C/C:\t\t{conta['numero_conta']}
               Titular:\t{conta['usuario']['nome']}
        """
        linha()
        print(textwrap.dedent(linhaa))
        linha()
    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao.lower() == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao.lower() == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao.lower() == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao.lower() == "u":
            criar_usuario(usuarios)

        elif opcao.lower() == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao.lower() == "l":
            listar_contas(contas)

        elif opcao.lower() == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()

#desafio sistema bancário dio
#https://github.com/renan1221
