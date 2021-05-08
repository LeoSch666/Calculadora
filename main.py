'''Author: Anibal Leonardo Schmitz
version 1.0'''
print("\n******************* Python Calculator *******************")

#solicita dois numeros ao usuario
num1 = float(input("Insira um numero: "))
num2 = float(input("Insira um numero: "))

#variaveis
soma = 0
sub = 0
mult = 0
div = 1

#Mostrar menu
opcao = int(input('Esolha uma operação: \n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n'))

#Operação com a opção escolhida pelo usuário
if opcao < 1 or opcao > 4:
    print('Opção inválida!! Insira um número entre 1 e 4!!')

if opcao == 1:
    soma = num1 + num2
    print('A soma de {} com {} é {}'.format(num1, num2, soma))

elif opcao == 2:
    sub = num1 - num2
    print('A subtração de {} com {} é {}.'.format(num1, num2, sub))

elif opcao == 3:
    mult = num1 * num2
    print('A multiplicação de {} com {} é {}.'.format(num1, num2, mult))

else:
    if num2 == 0:
        print('Não existe divisão por 0!!')
    else:
        div = num1 / num2
        print('A divisão de {} com {} é {}.'.format(num1, num2, div))
