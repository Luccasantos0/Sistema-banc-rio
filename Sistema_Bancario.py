menu = """


[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair


> """
    
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

        #Pergunta qual valor o usuario quer depositar
    if opcao == "0":
        valor = float(input("Informe o valor do depósito: "))

        #Verifica se o valor informado é positivo. Se for, adiciona ao saldo.
        #Também registra a operação no extrato com duas casas decimais.
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        # Caso o valor seja negativo ou zero, exibe uma mensagem de erro para o usuário
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    
    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        #Verificações
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= LIMITE_SAQUES
        
        #Mensagem informativa das verificações
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque ultrapassa o limite permitido de R$500.00.2")

        elif excedeu_saques:
            print("Operação falhou! Númeroo máximo de saques excedido.")

        
        # Se não excedeu saldo, limite ou número de saques, verifica se o valor é válido (positivo)
        # Se for, realiza o saque, atualiza o saldo, registra no extrato e incrementa o contador de saques
        # saldo -= valor: subtrai o valor sacado do saldo atual
        # extrato: registra a operação de saque com valor formatado
        # numero_saque: incrementa para controlar o limite diário de saques
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        # Se o valor informado para saque for negativo ou zero, exibe uma mensagem de erro
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Exibe o extrato das movimentações
    # O cabeçalho e rodapé são apenas elementos visuais (linhas de "=")
    # Se a variável 'extrato' estiver vazia (verificado com 'not extrato'), significa que não houve movimentações
    # Caso contrário, exibe todas as operações registradas (depósitos e saques)
    # Ao final, mostra o saldo atual formatado
    elif opcao == "2":
        print("\n================ EXTRATO ================")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "3":
        break
     #Digita operação que não conheço
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")







        