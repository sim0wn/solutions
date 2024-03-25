# Hello World!

* Desafio [1017](https://judge.beecrowd.com/pt/problems/view/1017)
* Categoria Iniciante

## Descrição

Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

## Solução
A aplicação deverá receber dois valores inteiros como entrada, sendo eles a duração da viagem em horas e a velocidade média durante o percurso.
Com isso, é possível calcular a distância percorrida multiplicando a velocidade pela duração.
Como o exercício informa, o automóvel tem autonomia de 12 km por litro de combustível; ou seja, se dividirmos a distância percorrida que calculamos por 12, obtemos quanto de combustível necessário para a viagem.

* [Python](main.py)
