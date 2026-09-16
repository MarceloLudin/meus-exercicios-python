#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
'''– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
import os 
os.system ("cls")

from datetime import datetime
ano_atual = datetime.now().year

ano_nascimento = int(input("\033[1;39mAno de Nascimento:\033[m "))

idade = ano_atual-ano_nascimento

if idade <= 9:
    print(f"O atleta tem {idade} anos.")
    print("Classificação MIRIM")
elif idade <=14:
    print(f"O atleta tem {idade} anos.")
    print("Classificação INFANTIL")
elif idade <=19:
    print(f"O atelta tem {idade} anos.")
    print("Classificação Júnior")
elif idade <=25:
    print(f"O atelta tem {idade} anos.")
    print("Classificação Sênior")
elif idade >25 and idade <124:
    print(f"O atleta tem {idade} anos.")
    print(f"Classificação MASTER")
else:
    print("\033[31mAno de Nascimento INVÁLIDO\033[m ")
