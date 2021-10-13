#Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele.

algo = input('Digite algo: ')
print(" O tipo primitivo desse valor é: ", type(algo))
print('Só tem espaços? ',algo.isspace())
print('è um número? ', algo.isnumeric())
print('É alfabetico? ', algo.isalpha())
print('É alfanumerico? ', algo.isalnum())
print('Esta em maiusculo? ',algo.isupper())
print('Esta em minusculo? ',algo.islower())
