#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de 
# triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
#Para formar um triângulo com três lados, a medida de qualquer um dos lados deve ser
# sempre menor do que a soma dos outros dois e maior do que a diferença absoluta entre eles
import os 
os.system ("cls")

print("\033[36m-*-\033m"*6)
print("\033[33mTipo de Triângulo\033[m")
print("\033[36m-*-\033[m"*6)

seg_1 = int(input("Dígite o primeiro seguimento:"))
seg_2 = int(input("Dígite o segundo seguimento: "))
seg_3 = int(input("Digíte o terceiro seguimento:"))

if seg_1 < seg_2+seg_3 and seg_2 < seg_3+seg_1 and seg_3 < seg_1+seg_2:
    print("Os seguimentos ácima podem formar um triângulo", end=" ")
    if seg_1 == seg_2 and seg_2 == seg_3:
        print("EQUILATÉRO!")
    elif seg_1 != seg_2 and seg_2 != seg_3 and seg_1 != seg_3:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("Não pode formar um TRIÂNGULO")
    exit()
