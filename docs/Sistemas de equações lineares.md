
![[sel-1.png]]

Para garantir a existência única de soluções, é necessário obter pelo menos um número de equações igual ao de variáveis, permitindo que todas variáveis sejam determinadas pelas equações disponíveis.

# Solução *numérica* de sistemas de equações lineares

Vamos partir sempre da hipótese de que os sistemas a serem solucionados são POSSÍVEIS e DETERMINADOS, possuindo pelo menos uma solução.
![[images/sel-2.png]]
Para um vetor ser a solução do problema, este vetor deve solucionar simultaneamente todas equações do sistema de equações lineares.
![[sel-3.png]]

# Métodos numéricos

Os [[Métodos numéricos]] para a resolução de sistemas lineares são divididos em duas categorias:
1. Métodos diretos
	1. São aqueles que, a menos de erros de arredondamento, fornecem a solução exata.
	2. Exemplos:
		1. [[Regra de Cramer]]
		2. [[Escalonamento]]
		3. [[Método de eliminação de Gauss]]
		4. [[Fatoração LU]]
2. Métodos iterativos 
	1. São aquele que,  a partir de um vetor inicial $\vec X^{(0)} = [\begin{array}  {a} x_1^{(0)},x_2^{(0)},...,x_n^{(0)} \end{array}]^{(t)}$ , gera uma sequencia de vetores $\vec X^{(1)}, \vec X^{(2)}, ...$ que sob determinadas condições converge para $\bar{x}$ solução de $A_x=b$.   
	2. Exemplos:
		1. [[Método iterativo de Gauss-Jacobi]]
		2. [[Método iterativo de Gauss-Seidel]]
		3. [[S.O.R (Seidel Over Relaxion)]]
		4. [[Descida do gradiente]] - Utilizado em [[Machine Learning]]


Os métodos diretos baseiam-se nas operações elementares sobre as linhas de uma matriz. A saber:
$$
(i) \text{  }  L_i \leftrightarrow L_j\text{ - (troca de linhas)}
$$
$$
(ii) \text{  }L_i \leftrightarrow kL_j \text{ - (k} \not = 0)
$$
$$
(iii) \text{  } L_i \leftrightarrow L_i + kL_j \text{ - (combinação de linhas)}
$$

![[sel-4.png]]![[sel-5.png]]
Dessa forma, é possível notar que se o sistema é Triangular Superior e o sistema de equações é linear, é possível obter a solução através da seguinte dedução geral:

![[Pasted image 20240422155624.png]]

Com isso, é dado o seguinte algoritmo para a solução computacional do problema:
![[Pasted image 20240422155733.png]]

Porém, este, só serve para Sistemas Lineares Triangularizados, ou seja, ainda precisamos definir como chegar em um sistema desses a partir de um sistema "cheio". 