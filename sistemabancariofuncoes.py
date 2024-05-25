# Listas para armazenar usuários e contas
usuarios = []
contas = []

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite diário.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque realizado: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Nenhuma movimentação registrada." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Usuário com este CPF já está cadastrado.")
            return

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta_corrente(cpf):
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break
    
    if not usuario:
        print("Erro: Usuário não encontrado.")
        return
    
    numero_conta = len(contas) + 1
    nova_conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario,
    }
    contas.append(nova_conta)
    print("Conta corrente criada com sucesso!")

# Variáveis globais
saldo = 0
limite = 500
extrato_texto = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Sair
=> """

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato_texto = deposito(saldo, valor, extrato_texto)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato_texto, numero_saques = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato_texto,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "3":
        extrato(saldo, extrato=extrato_texto)

    elif opcao == "4":
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Informe o CPF (somente números): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "5":
        cpf = input("Informe o CPF do usuário (somente números): ")
        criar_conta_corrente(cpf)

    elif opcao == "6":
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
