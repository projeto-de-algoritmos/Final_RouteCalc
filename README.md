# RouteCalc

**Número da Lista**: 6 </p>
**Conteúdo da Disciplina**: Grafos</p>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 16/0027225  |  Eduardo Yoshida |
| 16/0009758  |  João Lucas |

## Sobre 
O projeto tem como objetivo o cálculo da menor distância entre dois aeroportos utilizando algoritmo de Dijkstra.

## Screenshots
[!screenshot](img/img1.png)
[!screenshot](img/img2.png)
[!screenshot](img/img3.png)

## Instalação 
**Linguagem**: Python 2.7<br>
Para executar o projeto, deve-se, anteriormente, executar o comando.
Obs: recomenda-se a utilização de um virtualenv
```
pip install -r requirements.txt
```
## Uso 
Após instalados os requisitos. Deve-se executar na raiz do projeto:
```
python map.py
```

## Outros 
Foram utilizados datasets de aeroportos e rotas entre aeroportos obtidos em [https://github.com/jpatokal/openflights/tree/master/data](Open Flights), cujas distâncias(pesos das arestas do algoritmo de Dijkstra) foram calculadas a partir da latitude e longitude utilizando a biblioteca geopy.



