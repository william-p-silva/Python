

sal = float(input("Digite o valor em R$ do seu sálario: "))
val_casa = float(input("Digite o valor em R$ da casa que tem interesse: "))
prestacao = float(input("Digite em quantos anos você pretende pagar esta casa: "))

prestacao_meses = val_casa / (prestacao * 12) 

if prestacao_meses <= (sal * 0.30):
    print(f"\n\033[32mParabéns")
    print(f"O valor da casa em questão é {val_casa} pagos em {prestacao * 12} meses, com cada parcela sendo R$ {prestacao_meses:.2f}\033[m]\n")
else:
    print("\n\033[31mInfelizmente seu financiamento foi negado")
    print(f"O valor da casa em questão é {val_casa} pagos em {prestacao * 12} meses, com cada parcela sendo R$ {prestacao_meses:.2f}")
    print("Em nossa istituição para um financiamento ser aprovado as parcelas não podem ultrapassar 30% do salário\033[m]\n")