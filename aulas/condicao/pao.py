vl_pao = 0.65
dn_client = float(input('Coloque quanto dinheiro você tem! '))
if dn_client > vl_pao:
    qnt_pao_cli = int(dn_client / vl_pao)
    valor_pao_cli = float(dn_client / vl_pao)
    troco = dn_client - (qnt_pao_cli * vl_pao)
    print(f'Com o valor de {dn_client} você pode comprar {qnt_pao_cli} pães e seu troco é {troco}')
else:
    print('Infelismente você não tem dinheiro suficiente ')
