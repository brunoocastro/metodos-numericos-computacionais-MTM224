
Na verdade, estamos implementando "Zeros **Reais** de funções **reais**"

O zero de uma função, do ponto de vista geométrico, é onde a função (em Y) cruza o eixo X.
Do ponto de vista algébrico, por exemplo $f(x) = x - 3$, busca-se encontrar o valor de x no qual a resposta seja igual a zero $f(x) = 0$, nesse caso seria algo do tipo $x - 3 = 0 <-> x = 3 <-> f(3) = 3 - 3 = 0$, nesse caso, para obtermos $y = 0$ precisamos de $x = 3$


Dentro de zeros de funções, temos duas etapas:

- **Existência**
	- Método gráfico
	- [[Teorema de Bolzano]]
- **Refinamentos**
	- [[Método da bisseção]]
	- Método da Falsa posição (ou método das cordas)
	- Método de Newton-Raphson
	- Método das secantes

# Existência

## Método Gráfico
Consiste em transformar o problema F(x) = 0 num problema equivalente do tipo g(x) = h(x).
Se existir interseção entre o gráfico de g(x) e h(x), então o problema f(x) **admite solução**.

##### Exemplo 1:

```
f(x) = x-2

f(x) = 0 <-> x - 2 = 0 <-> x = 2

Neste caso, consideramos g(x) = x (primeiro lado da igualdade) e h(x) = 2 (segundo lado da igualdade).

Plotando o gráfico de ambas funções, encontraremos uma interseção no gráfico.
```


#### Exemplo 2:
```
f(x) = x² - 2

f(x) = 0 <-> x² - 2 = 0 <-> x² = 2

g(x) = x², uma parábola centrada em zero
h(x) = 2, uma reta no eixo y no ponto 2

Portanto, existe solução, pois existem dois pontos de interseção, um em x < 0 e outro em x > 0, ambos casos em y = 2
``` 

Também é possível decompor em duas funções simplificadas para que, da mesma forma, validemos se existe a interseção 

```
f(x) = x <-> x² - 2 = 0 <-> x * x - 2 = 0 <-> x * x = 2 <-> (x != 0)

x = 2/x

g(x) = x
h(x) = 2/x

Plotando os gráficos é possível validar, da mesma forma, que existe tal solução.
```

 