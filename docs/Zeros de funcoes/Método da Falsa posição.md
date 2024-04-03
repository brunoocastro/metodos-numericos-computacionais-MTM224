Método para resolução de problemas de [[Zeros de funções]]

Também chamado de:
- Método das cordas
- Método Regula False

# Problema:

Dados:
$f(x)$
- Intervalo $[a,b]$, tal que $f(a) . f(b) < 0$ 
- $f(x)$ contínua em $[a,b]$
- Dentro dos conceitos do [[Teorema de Bolzano]]


![[MetodoFalsaPosicao2024-04-03-15.53.53.excalidraw]]



> [!NOTE] Observação sobre [[Funções Trigonométricas]]
> 
> Sempre que falamos sobre funções trigonométricas, o ângulo da ferramentas que vamos utilizar (celular, calculadora, código) deve estar em [[RADIANOS]].
> 
> Seja uma função Seno, Cosseno, Tangente, ou qualquer outra função trigonométrica, se for fazer o cálculo em calculadora, deve-se configurar a calculadora para utilizar radianos.
> 
> Radianos = Quantos raios cabem nessa medida
> $2 *\pi * r$ em Radiano = 360º, ou seja, se o raio do circulo for 1 metro, o perimetro (a borda do circulo) mede em tamanho $2*\pi$ metros, ou seja, 6,2831 metros.

# Validar existência de solução

Para validar a existência de solução, podemos utilizar tanto o [[Teorema de Bolzano]] quanto o [[Método Gráfico]], desde que a função satisfaça as condições dos teoremas.

# Estimativa de execuções

Não é possível estimar o número de execuções, portanto, gaste o tempo antes de começar a execução, de forma a melhorar o intervalo inicial de execução do método para evitar maiores trabalhos.

Ou seja, chute diferentes valores iniciais de $[a,b]$ de forma a continuar satisfazendo o [[Teorema de Bolzano]], ou seja, mantendo $f(a)*f(b) < 0$.

Isso pode te poupar um ENORME trabalho, faça com que os valores de $f(a)$ e $f(b)$ estejam bem próximos de zero, assim terá de fazer poucas iterações do método.

