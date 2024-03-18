
Conceitualmente, o método da bisseção divide o intervalo em dois. Dentre as duas divisões, precisamos identificar onde está a solução. Caso esteja no primeiro intervalo, descartamos o intervalo remanescente e voltamos a dividir o intervalo restante, de forma a ir restringindo iterativamente o intervalo, ao ponto de restar somente o valor que buscamos.

# Erro absoluto
É a diferença entre o valor exato $(x)$ de uma grandeza e o seu valor aproximado $(\bar x)$
$$
E_{A_x} = x - \bar x
$$
Na prática, a definição do erro absoluto tem pouca utilidade - pois não conhecemos o valor exato $(x)$

Utilizamos, de fato, um limitando superior para o erro absoluto.

**Ex 1:** $\sqrt 2 \in (1.4;1.5)$

Para qualquer aproximação $\sqrt 2$ no intervalo $(1.4;1.5)$ temos $E_{A_{\sqrt 2}} < 0.1$

**Ex 2:** $\pi \in (3.14;3.15)$
Para qualquer aproximação de $\pi$ no intervalo (3.14;3.15) temos $E_{A_{\pi}} < 0.01$

# Erro relativo ($E_R$)
$$
E_{R_X} = \frac {E_{A_X}}{\bar X}
$$

Dessa forma, estamos "normalizando" o erro absoluto, na prática, temos uma medida percentual de erro. Isso nos traz uma informação muito mais significativa que o Erro Absoluto, pois permite compreender a proporção do erro observado, e não somente o seu valor absoluto.

Neste caso, podemos dizer que o $E_{R_X}$ representa muito melhor o erro do que o $E_{A_X}$


### Algoritmo em Pseudo-código



### Exemplo aplicando o método

$f(x) = x² - 2$


Dado intervalo (arbitrário) code

```python
from bissecao import Bissecao

ex1 = Bissecao(1.4, 1.5, lambda x: x**2 - 2)
ex1.calculate_root()
```

