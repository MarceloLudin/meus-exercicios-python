# IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
import os 
os.system ('cls')
print("\033[34m-_-_-\033[m"*3)
print("Cálculo do IMC")
print("\033[34m-_-_-\033[m"*3)

peso_atual = float(input("Dígite seu peso atual (Kg)"))
altura = float(input("Dígite sua altura atual (M)"))

imc = peso_atual/(altura**2)

print(f'O peso atual é {peso_atual:.2f}Kg')
print(f"O IMC dessa pessoa é de {imc:.2f}")
if imc< 18.5:
    print('\033[31mA pessoa está abaixo do peso\033[m')
if imc >= 18.5 and imc <= 25:
    print("\033[34mParabéns está com o peso ideal!\033[m")
if imc >=25 and imc <=30:
    print("\033[33mA pessoa está com sobrepeso!\033[m")
if imc >= 30 and imc <= 40:
    print('\033[31mA pessoa está com obesidade\033[m')
if imc > 40:
    print('\033[31mA PESSOA ESTÁ COM OBESIDADE MORBIDA PROCURE ORIENTEAÇÃO MÉDICA\033[m')
    
    
