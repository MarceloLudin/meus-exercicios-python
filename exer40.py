#Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO – Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

import os
os.system ("cls")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1+n2)/2

if media<5.0:
    print(f"Você está REPROVADO\nSua média é {media}")
elif media>=5.0 and media <=6.9:
    print(f"Você está de RECUPERAÇÃO\nSua nota é {media}")
else:
    print(f"Você está APROVADO\nSua nota é {media:.1f}")
    

