# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Insira um valor em metros: '))
print('O valor {}m em centímetros é igual a {:.1}'.format(n, n * 100))
print('O valor {}m em milímetros é igual a {:.1}'.format(n, n * 1000))
print('Deu tudo certo ;)')
