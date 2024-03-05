# -*- coding: utf-8 -*-

# recebe a entrada do programa e separa entre centavos e reais
reais, centavos = [int(value) for value in input().split(".")]

# para evitar problemas na divisão com o ponto decimal, transforma-se tudo
# para centavos, considerando que cada real equivale a cem centavos
centavos += reais * 100

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    # divide o total pelo equivalente a cada nota em centavos
    print(f"{int(centavos//(nota*100))} nota(s) de R$ {nota:.2f}")
    # atribui o resto da divisão ao total
    centavos %= nota * 100

print("MOEDAS:")
for moeda in moedas:
    # divide a quantidade total pelo equivalente de cada moeda em centavos
    print(f"{int(centavos//(moeda*100))} moeda(s) de R$ {moeda:.2f}")
    # atribui o resto da divisão ao total
    centavos %= moeda * 100
