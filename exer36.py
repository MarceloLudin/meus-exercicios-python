#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("\033[34m-=-\033[m" *10)
print("\033[33m   EMPRÉSTIMO BANCÁRIO \033[m")
print("\033[34m-=-\033[m" *10)

valor_casa = float(input("Digite o valor da casa R$")) #PERGUNTA O VALOR DA CASA

salario_comprador = float(input("Qual o salário do comprador: R$")) #PERGUNTA O SALÁRIO DO COMPRADOR

anos_pagamento = int(input("Em quantos anos ele pretende pagar? ")) #PERGUNTA QUANTOS MESES PRETENDE PAGAR

meses_pagamento = anos_pagamento*12

valor_parcela = valor_casa/meses_pagamento

trinta_salario = salario_comprador*0.30

if valor_parcela>= trinta_salario:
    print(f"Para pagar uma casa de R$\033[32m{valor_casa:.2f}\033[m em {anos_pagamento} anos a prestação será de R$\033[32m{valor_parcela:.2f}\033[m ") 
    print("Não podemos aprovar o empréstimo! ")
else:
    print(f"Parabéns seu emprestímo foi \033[33maprovado\033[m com o valor da casa de R$\033[32m{valor_casa:.2f}\033[m com parcela de R$\033[32m{valor_parcela:.2f} \033[m")