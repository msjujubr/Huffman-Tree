# Implementação do Código de Huffman
![Python](https://img.shields.io/badge/Linguagem-Python-green)
![VSCode](https://img.shields.io/badge/IDE-VSCode-informational)
![ISO](https://img.shields.io/badge/ISO-Linux-blueviolet)

### 📖 Sumário
- [Introdução](#introdução)
- [O Algoritmo](#o-algoritmo)
  - [Construção da Árvore Huffman](#construção-da-árvore-huffman)
  - [Geração dos Códigos Binários](#geração-dos-códigos-binários)
  - [Complexidade do Algoritmo](#complexidade-do-algoritmo)
- [Implementação, Entradas e Saídas](#implementação-entradas-e-saídas)
- [Referências](#referências)
  
## Introdução
O algoritmo de Huffman foi desenvolvido por David A. Huffman em 1952, enquanto ele era estudante de pós-graduação no MIT, como parte de um trabalho para a disciplina de Teoria da Informação, ministrada por Robert Fano. Esse algoritmo tornou-se uma das técnicas mais eficientes para compressão de dados sem perdas, reduzindo o espaço de armazenamento necessário ao atribuir códigos de tamanhos diferentes para cada símbolo, de acordo com sua frequência de ocorrência.

A ideia principal é: símbolos mais frequentes recebem códigos binários menores, enquanto símbolos menos frequentes recebem códigos maiores, garantindo eficiência global. Essa técnica utiliza códigos prefixos, garantindo que nenhum código atribuído a um símbolo seja prefixo do código de outro, evitando ambiguidades durante a decodificação.

Neste trabalho, apresento uma implementação do algoritmo de Huffman em Python, capaz de realizar a compressão de pequenos trechos de texto utilizando essa técnica.

## O Algoritmo
O processo básico pode ser descrito por meio do seguinte pseudocódigo:
> ```
> HUFFMAN(S)
>     fila de prioridade Q com um nó para cada símbolo em S
>     enquanto |Q| > 1:
>         remova os dois nós x e y com menores frequências de Q
>         crie um novo nó z com:
>         freq[z] = freq[x] + freq[y]
>         esq[z] = x
>         dir[z] = y
>         insira z em Q
> retorne o único nó restante em Q
> ```

### Construção da Árvore Huffman
A construção da árvore de Huffman tem como objetivo organizar os símbolos em uma estrutura hierárquica que reflete suas frequências relativas, permitindo a atribuição eficiente de códigos. O processo segue os seguintes passos:
- Para cada símbolo do conjunto de dados, cria-se um nó folha, atribuindo a esse nó a respectiva frequência de ocorrência;
- Todos os nós são inseridos numa fila de prioridade, organizada por ordem crescente de frequência (min-heap).
- Enquanto existir mais do que um nó na fila de prioridade:
    - Extraem-se os dois nós com as menores frequências;
    - Cria-se um novo nó interno, designando os dois nós extraídos como seus filhos;
    - A frequência do novo nó é definida como a soma das frequências dos seus filhos;
    - O nó resultante é reinserido na fila de prioridade.

Quando restar apenas um nó na fila, este constitui a raiz da árvore de Huffman, representando a estrutura completa.

### Geração dos Códigos Binários
A partir da árvore construída, procede-se à atribuição dos códigos binários a cada símbolo, mediante o percurso dos caminhos da raiz até a cada folha:
- A cada transição para um filho esquerdo, associa-se o bit 0;
- A cada transição para um filho direito, associa-se o bit 1;
- O código de cada símbolo corresponde à sequência de bits acumulada ao longo do percurso desde a raiz até à respectiva folha.

Após a construção da árvore e a geração dos códigos binários, é possível calcular o tamanho final da mensagem comprimida. Esse cálculo é importante para avaliar a eficiência da compressão obtida pelo algoritmo de Huffman. O comprimento total da mensagem é dado por:

<p align="center">

$$
Comprimento\ total = \sum_{i=1}^{n} (f_i \times l_i)
$$

</p>

onde: 
- $f_i$: frequência do símbolo
- $l_i$: comprimento do código do símbolo, em bits
	​
### Complexidade do Algoritmo
A análise de complexidade do algoritmo de Huffman é fundamental para compreender sua eficiência e justificar seu amplo uso em sistemas de compressão. Essa análise considera separadamente cada etapa do processo — desde a leitura dos dados até a geração final dos códigos —, permitindo uma visão completa do custo computacional envolvido

O algoritmo inicia com a leitura da entrada para contabilizar o número de ocorrências de cada símbolo. Esse procedimento requer percorrer toda a sequência de símbolos, o que resulta em uma complexidade linear: $O(n)$

<div align="center">

$$O(n)$$, sendo $n$ o total de símbolos.

</div>

Após a contagem, são criados k nós, um para cada símbolo distinto, e todos são inseridos em uma fila de prioridade (min-heap). Como este processo é realizado usando uma _min-heap_, onde a extração do mínimo e a inserção de um novo elemento são operações O(log k), e repetimos isso (k-1) vezes, o custo total da etapa central é: 

<div align="center">

$O(k logk)$

</div>

Este é o termo mais significativo da parte estrutural do algoritmo, pois envolve operações repetidas sobre uma estrutura ordenada. Combinando todas as etapas, a complexidade total do algoritmo de Huffman é dada por:

<div align="center">

$O(n+klog⁡k)$

</div>

Isso significa que, na prática, o algoritmo se comporta de forma linear em relação ao tamanho da entrada. Para entradas grandes comuns, como na compressão de documentos, o custo maior é proveniente da leitura dos dados (O(n)). Apenas em cenários onde há grande variação de símbolos, a complexidade se aproxima de O(k log k), mas mesmo neste caso o algoritmo mantém-se eficiente. O algoritmo de Huffman é considerado ótimo entre os códigos prefixos, e sua complexidade é assintoticamente a melhor possível para algoritmos baseados na ordenação de frequências.

## Implementação, Entradas e Saídas
A implementação proposta lê textos do arquivo _input.dat_, onde cada linha não vazia é tratada como um texto independente. Para cada linha, calcula-se a frequência das palavras, não opera por caracter. A compressão opera por termo, de modo que cada termo distinto recebe um código de Huffman próprio. Todos esses dados são organizados em formato JSON e armazenados no arquivo output.dat, permitindo uma representação estruturada da compressão. Tanto _input.dat_ quanto _output.dat_ devem estar dentro da pasta _data_.

### Referências
- [MIT OCW – Ch. 19: Técnicas de prova (18.310)](https://ocw.mit.edu/courses/18-310-principles-of-discrete-applied-mathematics-fall-2013/e61d70ff3cab49cb2f2352b758acbb49_MIT18_310F13_Ch19.pdf)
- [MIT OCW – Lecture 19 (6.046J Design & Analysis of Algorithms)](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2012/388115265a456321c4a5d19dc9e05281_MIT6_046JS12_lec19.pdf)

<div> 
  <a href="https://www.youtube.com/@msjujubr" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" target="_blank"></a>
  <a href="https://instagram.com/msjujubr" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
 	<a href="https://www.twitch.tv/msjujubr" target="_blank"><img src="https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white" target="_blank"></a>
  <a href = "mailto:juliamourasouza10@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://www.linkedin.com/in/msjujubr/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
</div>
