
Conceitualmente, o método da bisseção divide o intervalo em dois. Dentre as duas divisões, precisamos identificar onde está a solução.
- Primeiramente validamos se o ponto médio (o ponto exato onde o intervalo foi dividido) é a solução. Caso seja, já encontramos a resposta.
- Caso contrário, só temos duas possibilidades:
	- Ou está na primeira metade do intervalo
	- Ou está na segunda metade do intervalo

Caso esteja no primeiro intervalo, descartamos o intervalo remanescente, visto que certamente nossa resposta está no primeiro intervalo. Após descartar o segundo intervalo, voltamos a dividir o intervalo restante, de forma a ir restringindo iterativamente o intervalo, ao ponto de restar somente o valor que buscamos, de acordo com um erro mínimo estabelecido.

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


# Como encontrar a solução

A solução pode se dar convergindo tanto pela Imagem quanto pelo Domínio.

Para este problema, fornecemos um erro máximo a ser utilizado, e este erro deve ser medido, a cada iteração, tanto pela imagem quanto pelo domínio.

Dessa forma, caso atingido o erro máximo, a solução é valida, seja ela pela imagem ou pelo domínio, portanto, precisamos validar em nosso algoritmo ambas soluções.

$$
| b - a | < \epsilon
$$
$$ ou $$
$$
| f(pm) | < \epsilon
$$

- Sendo $\epsilon$ a tolerância desejada, ou seja, o erro máximo para considerarmos uma resposta.

Qualquer uma das ocorrências a cima devem ser consideradas como uma resposta válida, devida aplicação do teorema dos limites, ocasionando a uma redução tão grande do intervalo $[a,b]$ que só nos resta um ponto, sendo esse ponto a solução para todas as iterações anteriores.
# Algoritmo em Pseudo-código

### [[Algoritmo]]
Uma sequencia lógica finita de passos para a resolução de um problema.

```bash
1. Entradas
	1. Entre com a função f(x)=
	2. Entre com o valor de a=
	3. Entre com o valor de b=
	4. Entre com a tolerância epsilon=
2. Método da bisseção
	1. enquanto 
		   |b - a| > epsilon, faça: (Essa condição valida o encontro da solução pelo dominio)
			1. avalie f(a)
			2. avalie f(b)
			3. calcule pm = ((a+b)/2)
			4. avalie f(pm)
			5. se 
			   |f(pm)| < epsilon, então: (Essa condição valida o encontro da solução pela imagem)
				1. escreva("PM é a solução. A convergencia ocorreu pela imagem.")
				2. saia do programa
			   fim-se
			6. se
				f(a)*f(pm) < 0
					1. b = pm
				se-não
					1. a = pm
				fim-se
		fim-enquanto
3. Exibir solução
	1. escreva("A convergencia ocorreu pelo dominio.")
	2. escreva("A solução é", pm=((a+b)/2))
``` 


# Estimativa do número de iterações

Dados $a0$, $b0$ e $\epsilon$ , para descobrir o número de iterações N, temos:
$$
N > \frac {log({b_0 - a_0}) - log(\epsilon)} {log(2)}
$$
### Exemplo aplicando o método

$f(x) = x² - 2$


Dado intervalo (arbitrário) code

```python
from .code.bissecao import Bissecao

ex1 = Bissecao(lambda x: x**2 - 2, 1.4, 1.5)
ex1.calculate_root()
```

