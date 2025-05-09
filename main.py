
extrato=[]
saldo = 0.00
i=0    
limite_de_saque=0

while True:
    print(" menu ".center(20, "*"))
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Saldo")
    print("5 - Sair")

    opcao= input("\n Escolha uma das opções:") 

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        print(f"R$ {valor:.2f} depositado com sucesso")
        extrato.append(('Depósito:', valor))
        saldo += float(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if valor < saldo and  limite_de_saque < 3 and valor < 500:
            print(f"R$ {valor} retirado com sucesso")
            extrato.append(('Retirado:', -valor))
            saldo += float(-valor)
            limite_de_saque +=1
        else:
            print(f"Não foi possivel efetuar o saque.\nSeu saldo é de R${saldo:.2f} e já efetuou {limite_de_saque} saques. \nVolte amanhã pra efetuar num novo saque! ")        
    elif opcao == "3":
        print(" Extrato ".center(18, "*"))
        for i in extrato:
            print(f"{i}")
        print(f"Seu saldo é de R$ {saldo:.2f}")    
    elif opcao == "4":
        print(f"Seu saldo é de R$ {saldo:.2f}")      
    elif opcao == "5":
        print("Até a proxima!")
        break
    else:
        print("Opção invalida")






    


