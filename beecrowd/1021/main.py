# -*- coding: utf-8 -*-

# recebendo a entrada do programa e convertendo para valor numérico de ponto
# flutuante
value = float(input())

# exibindo a saída do programa e calculando a quantidade necessária de cédulas
# e moedas
print(
    f"""NOTAS:
{int(value//100)} nota(s) de R$ 100.00
{int(value%100//50)} nota(s) de R$ 50.00
{int(value%100%50//20)} nota(s) de R$ 20.00
{int(value%100%50%20//10)} nota(s) de R$ 10.00
{int(value%100%50%20%10//5)} nota(s) de R$ 5.00
{int(value%100%50%20%10%5//2)} nota(s) de R$ 2.00
MOEDAS:
{int(value%100%50%20%10%5%2//1)} moeda(s) de R$ 1.00
{int(value%100%50%20%10%5%2%1//0.5)} moeda(s) de R$ 0.50
{int(value%100%50%20%10%5%2%1%0.5//0.25)} moeda(s) de R$ 0.25
{int(value%100%50%20%10%5%2%1%0.5%0.25//0.1)} moeda(s) de R$ 0.10
{int(value%100%50%20%10%5%2%1%0.5%0.25%0.1//0.05)} moeda(s) de R$ 0.05
{int(value%100%50%20%10%5%2%1%0.5%0.25%0.1%0.05//0.01)} moeda(s) de R$ 0.01"""
)
