#faça um programa que leia um valor em metro e o exiba convertido em centimetro e milimetro.

medida = float(input('Digite um valor em metro: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

