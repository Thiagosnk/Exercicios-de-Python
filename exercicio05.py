#Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e antecessor.

num = int(input('Digite um numero: '))
a = num - 1 #antecessor
s = num + 1 #sucessor

print(' Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(num, a, s))

#segunda forma de fazer

num = int(input('Digite um numero: '))


print(' Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(num, (num - 1), (num + 1)))