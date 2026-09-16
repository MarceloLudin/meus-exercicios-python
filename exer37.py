#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


numero_inteiro  = int(input("Digite um número inteiro: "))

print(""" Escolha uma das bases para opção: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para hexadecimal""")

opcao = int(input("Dígite sua opção: "))

if opcao == 1:
    print(f"{numero_inteiro} convertido para binário é igual a {bin(numero_inteiro)[2:]}")
elif opcao == 2:
    print(f"{numero_inteiro} convertido em Octal é igual a {oct(numero_inteiro)[2:]}")
elif opcao == 3:
    print(f"{numero_inteiro} convertido para Exadecimal é igual a {hex(numero_inteiro)[2:]}")
else:
    print("\033[31;43mOPCÇÃO INVALIDA\033[m ")