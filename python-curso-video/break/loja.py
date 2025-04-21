



total = pro_mais_1000  = c = 0
pro_barato = ' '
print("Loja Baratão")

while True:
        continua = ' '
        pro = input("Qual o nome do produto? ")
        pr_pro = float(input("Qual o valor do Produto? "))
        c += 1
        total += pr_pro
        if pr_pro >= 1000:
            pro_mais_1000 += 1 
            
        if c == 1 or pr_pro < pr_pro_barato:
            pr_pro_barato = pr_pro
            pro_barato = str(pro)
        
        while continua not in 'sn':
            continua = input("Quer continuar? [S/N] ").lower().strip()[0]
        if continua == 'n':
                break


print(f"O valor total da compra foi {total}\nO produto mais barato foi {pro_barato} por R$ {pr_pro_barato}\nTivemos {pro_mais_1000} produtos acima de R$ 1000")

