

print("=====================""loja""=====================")
valor = float(input("\nDigite em R$ o valor de suas compras: R$ "))
print("\nQual seria a forma de pagamento")
print("[1] Á vista no dinheiro/pix (10% off); ")
print("[2] Á vista no cartão (5% off); ")
print("[3] Em até 2x no cartão (preço normal); ")
print("[4] 3x ou mais no cartão (20% de juros). ")
print("\n=====================""loja""=====================")

escolha = int(input("\nEscolha uma das opções (apenas números inteiros): "))
while escolha != -1 :
    if escolha == 1:
        pag = valor - (valor * 0.10)
        print(f"\nPagando no dinheiro ou pix você tem direito a 10% off. O valor final da sua compra sai por R${pag:.2f}\n")
        break
    elif escolha == 2:
        pag = valor - (valor * 0.05)
        print(f"\nPagando á vista no cartão você tem direito a 5% off. O valor final da sua compra sai por R${pag:.2f}\n")
        break
    elif escolha == 3:
        pag = valor
        parc = valor / 2
        print(f"\nPagando no cartão em 2x você não tem desconto e nem juros. O valor final da sua compra sai por R${pag:.2f} com cada parcela sendo R${parc:.2f}\n")
        break
    elif escolha == 4:
        parc = int(input("Quantas parcelas? "))
        if parc > 2 and parc < 11:
            pag = valor + (valor * 0.20)
            parc = pag / parc 
            print(f"\nPagando no cartão em 3x ou mais cobramos juros de 20%. O valor final da sua compra sai por {pag:.2f} com cada parcela sendo R${parc:.2f}\n")
            break
        elif parc > 0 and parc <= 2:
            print("Você pode estar perdendo descontos, tem certesa dessa opção? ")
            print("Digite [s] para sim e [n] para não ")
            escolha2 = input("Escolha uma das opções [s] ou [n]: ").lower()
            if escolha2 == 's':
                pag = valor + (valor * 0.20)
                parc = pag / parc 
                print(f"\nPagando no cartão em sem descontos cobramos juros de 20%. O valor final da sua compra sai por {pag:.2f} com cada parcela sendo R${parc:.2f}\n")
                break
            elif escolha2 == 'n':
                print("\n=====================""loja""=====================")
                valor = float(input("\nDigite em R$ o valor se suas compras: R$ "))
                print("\nQual seria a forma de pagamento")
                print("[1] Á vista no dinheiro/pix (10% off); ")
                print("[2] Á vista no cartão (5% off); ")
                print("[3] Em até 2x no cartão (preço normal); ")
                print("[4] 3x ou mais no cartão (20% de juros). ")
                print("\n==============================================")

                escolha = int(input("Escolha uma das opções (apenas números inteiros): "))
                print('\n')
                
        else:
            print("\n\033[31m[ERRO]\033[mVocê excedeu o número de parcelas permitidas pela loja ou colocou dados invalidos ")
            print("\n=====================""loja""=====================")
            valor = float(input("\nDigite em R$ o valor se suas compras: R$ "))
            print("\nQual seria a forma de pagamento")
            print("[1] Á vista no dinheiro/pix (10% off); ")
            print("[2] Á vista no cartão (5% off); ")
            print("[3] Em até 2x no cartão (preço normal); ")
            print("[4] 3x ou mais no cartão (20% de juros). ")
            print("\n==============================================")

            escolha = int(input("Escolha uma das opções (apenas números inteiros): "))
            print('\n')
            
    else:
        print("[ERRO]\nOpçõa invalida ")
        escolha = int(input("Escolha uma das opções (apenas números inteiros): "))

