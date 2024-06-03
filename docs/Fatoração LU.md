Também conhecido por Decomposição LU

Consiste em fatorar a matriz A do sistema linear $Ax = b$, no produto de duas matrizes L (Lower -  triangular inferior) com $L_{i,i} = 1; i=1,...,n$, por U (Upper - Triangular superior).

![[FATLU-1.png]]
> [!NOTE] Primeira Observação
> A faturação ocorre sobre a matriz A e não sobre $[A | b ]$ (matriz aumentada)

![[FATLU-2.png]]
Assim teremos dois sistemas lineares para resolver, baseado em duas novas matrizes, sendo uma delas a matriz U, resultado final das operações, e a matriz L, que é a matriz dos coeficientes utilizados para chegar na matriz U. Dessa forma, conseguimos resolver o sistema $Ax = b$ fazendo $LUx = b$, pois estes são equivalentes.

![[FATLU-3.png]]

Agora primeiro nos preocupamos em encontrar $y_1$, $y_2$ e $y_3$, e através deles, encontramos posteriormente os valores de $x_1$, $x_2$ e $x_3$, que são a solução do sistema inicial.

![[FATLU-4.png]]
