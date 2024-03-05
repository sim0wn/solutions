# Notas e Moedas

* Desafio [1021](https://judge.beecrowd.com/pt/problems/view/1021)
* Categoria Iniciante

## Descrição

Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

## Solução

A resolução desse desafio é bem simples, e é necessário apenas calcular divisão e o resto da divisão. Isto é, dividimos o valor de entrada pela maior unidade disponível (que nesse caso é a cédula de 100 reais), e calculamos as unidades seguintes com base no que restou da divisão pela última unidade.

Usando de exemplo 18 reais, temos que:

* A maior unidade disponível pela qual 18 pode ser dividido é 10, sendo que 18 dividido por 10 é 1 e resta 8;
* pegamos o resto da última divisão (8) e temos que a maior unidade pela qual 8 pode ser dividido é 5, e resta 3;
* restando 3, ele pode ser dividido por 2 e sobra 1;
* dessa forma, mais uma moeda de 1 real pode completar o valor, e ele não terá mais resto divisível.

O resultado da execução do programa para a entrada de 18 deverá ser:

```
NOTAS:
0 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
0 nota(s) de R$ 20.00
1 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
1 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
0 moeda(s) de R$ 0.01
```

Tendo essa lógica em mente, o código do programa deverá seguir o seguinte fluxo:

> Recebe o valor de entrada;<br>
> divide o valor de entrada por 100;<br>
> calcula o resto da divisão do valor de entrada por 100 e divide por 50;<br>
> e repete sucessivamente com as outras unidades possíveis.:


* [Python](main.py)
