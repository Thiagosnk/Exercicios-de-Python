#faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considere o valor do dollar atual.

real =  float(input('Quando você tem na carteira? R$: '))
dolar = real / 5.06
euro = real / 6.13
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}'.format(real, dolar, euro))


