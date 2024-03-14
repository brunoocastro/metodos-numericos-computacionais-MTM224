
Na verdade, estamos implementando "Zeros **Reais** de funções **reais**"


Dentro de zeros de funções, temos duas etapas:

- Existência
	- Método gráfico
	- Teorema de Bolzano
- Refinamentos
	- Método da bisseção
	- Método da Falsa posição 
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


# Teorema de Bolzano

Para uma função possuir solução, ela precisa
- Ser continua no intervalo $[a,b]$ 
- Função em a vezes em b tem que ser menor do que zero



> [!NOTE] Definição do teorema de Bolzano
> Se $f(x)$ é contínua em $[a,b]$ e $f(a) \cdot f(b) < 0$, então existe, pelo menos, um ponto $x = \xi$ no intervalo $(a,b)$ tal que $f(\xi) = 0$. 

 
# Método da bisseção
Conceitualmente, o método da bisseção divide o intervalo em dois. Dentre as duas divisões, precisamos identificar onde está a solução. Caso esteja no primeiro intervalo, descartamos o intervalo remanescente e voltamos a dividir o intervalo restante, de forma a ir restringindo iterativamente o intervalo, ao ponto de restar somente o valor que buscamos.