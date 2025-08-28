def caixa_eletronico():
    saldo = 1000.00  
    while True:
        
        print("Caixa Eletrônico")
        print("(1) Sacar")
        print("(2) Depositar")
        print("(3) Ver Saldo")
        print("(4) Sair")
        
        
        opcao = int(input("Opção: "))
        
        if opcao == 1:  
            valor_saque = float(input("Valor para sacar: R$ "))
            if valor_saque <= saldo:
                saldo -= valor_saque
                print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente!")
        
        elif opcao == 2:  
            valor_deposito = float(input("Valor para depositar: R$ "))
            saldo += valor_deposito
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        
        elif opcao == 3:  
            print(f"Seu saldo atual é: R$ {saldo:.2f}")
        
        elif opcao == 4:  
            print("Obrigado por usar nossos serviços!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

caixa_eletronico()
