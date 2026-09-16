#Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou 
# do tempo do alistamento. Seu programa também deverá
# mostrar o tempo que falta ou que passou do prazo.
import os 
os.system ("cls")

from datetime import datetime
ano_atual = datetime.now().year

homem_mulher = (input("""Você é homem ou mulher?\n [ 1 ] Homem \n [ 2 ] Mulher\nSelecione uma opção: """))

if homem_mulher == "1":
    ano_nascimento = int(input("Que ano você nasceu? "))
else:
    print("Você é Mulher, Seu alistamento não é Obrigatório!")
    exit()

idade = ano_atual-ano_nascimento
prazo = idade-18
alistamento_atrazado = ano_atual-prazo #CÁLCULA EM QUE ANO ERA PARA TER FEITO O ALISTAMENTO!
if idade == 18:
    print(f"Está na hora de se alistar \nVocê já tem {idade} anos!")
elif idade < 18:

    print(f"Não está na hora de se alistar ainda \nVocê tem {idade} anos!")
    print(f"Faltam {18-idade } anos para seu alistamento! ")
    print(f"Seu alistamento será em {ano_atual + 18-idade}")
elif idade > 18:
    print(f"Já passou da idade do alistamento\nVocê tem {idade} anos!")
    print(f"O prazo era até {idade-18} anos atrás!")
    print(f"Seu alistamento foi em {alistamento_atrazado}.")
 

