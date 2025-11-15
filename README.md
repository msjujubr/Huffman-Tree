# Implementação do Código de Huffman
![Python](https://img.shields.io/badge/Linguagem-Python-green)
![VSCode](https://img.shields.io/badge/IDE-VSCode-informational)
![ISO](https://img.shields.io/badge/ISO-Linux-blueviolet)

### 📖 Sumário
- [Introdução](#introducao)
- [O Algoritmo](#o-algoritmo)
  - [Funcionamento](#funcionamento)
  - [Construção da Árvore Huffman](#construcao-da-arvore-huffman)
  - [Geração dos Códigos Binários](#geracao-dos-codigos-binarios)
- [Compilação, Entradas e Saídas](#compilação-entradas-e-saídas)
  - [Input.dat](#inputdat)
  - [Output.dat](#outputdat)
- [Referências](#referências)]
  
## Introdução
O algoritmo de Huffman foi desenvolvido por David A. Huffman em 1952, enquanto ele era estudante de pós-graduação no MIT, como parte de um trabalho de curso em Teoria da Informação, ministrado por Robert Fano. Ele surgiu como uma solução eficiente para compressão de dados sem perdas, buscando reduzir o espaço necessário para armazenar informações, aproveitando a frequência de ocorrência de símbolos em uma mensagem. A ideia central era representar símbolos mais comuns com códigos binários mais curtos e símbolos menos frequentes com códigos mais longos, otimizando o uso do espaço de armazenamento.

O princípio básico do algoritmo de Huffman é a codificação de prefixo, que garante que nenhum código atribuído a um símbolo seja prefixo de outro. Isso evita ambiguidades na decodificação. A eficiência do método se baseia em analisar a frequência de cada símbolo no conjunto de dados e construir uma representação binária que minimize o número total de bits necessários para codificar a mensagem completa.

Neste trabalho, apresento uma aplicação em linguagem Python do algoritmo, capaz de realizar a compressão de pequenos trechos de texto utilizando o código de Huffman como método.

## O Algoritmo
> ```
> HUFFMAN(S)
>     fila de prioridade Q com um nó para cada símbolo em S
>     enquanto |Q| > 1:
>         remova os dois nós x e y com menores frequências de Q
>         crie um novo nó z com:
>         freq[z] = freq[x] + freq[y]
>         left[z] = x
>         right[z] = y
>         insira z em Q
> retorne o único nó restante em Q
> ```

### Construção da Árvore Huffman
A construção da árvore de Huffman tem como objetivo organizar os símbolos em uma estrutura hierárquica que reflecte suas frequências relativas, permitindo a atribuição eficiente de códigos. O processo segue os seguintes passos:
- Para cada símbolo do conjunto de dados, cria-se um nó folha, atribuindo a esse nó a respetiva frequência de ocorrência;
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
- O código de cada símbolo corresponde à sequência de bits acumulada ao longo do percurso desde a raiz até à respetiva folha.

## Aplicação, Entradas e Saídas
A implementação proposta lê textos do arquivo _input.dat_, separando-os por linhas vazias, e para cada texto calcula a frequência das palavras, constrói a árvore de Huffman e gera códigos binários de cada uma. Cada palavra é então substituída pelo seu código correspondente, produzindo um texto comprimido. Todas as informações — frequências, árvore, códigos, texto original e comprimido — são organizadas em JSON e gravadas em _output.dat_, permitindo armazenar os dados de forma compacta e estruturada. Ambos arquivos _input.dat_ e _output.dat_ devem ser armazenados em uma pasta _data_. 

### Referências
- [Documento Prática](docs/documento_atividade01.pdf)
- [1]: https://youtu.be/NqUSJWec3pM?si=C33oaYJOJ01Xs7y5  
  *Vídeo do Cosmopolita explicando o Jogo da Vida*
- [2]: https://archive.org/details/a-new-kind-of-science-stephen-wolfram-z-lib.org/mode/2up
  *Livro completo: A New Kind of Science – Stephen Wolfram (2002)*
- [3]: https://github.com/MasterGos/magisterka/blob/master/Materialy%20z%20sieci/AOP/Wiley%20-%20Wooldridge,%20An%20Introduction%20to%20Multi%20Agent%20Systems%20(OCR%20guaranteed%20on%20full%20book).pdf
  *Link do GitHub do magisterka com o livro: An Introduction to Multi Agent Systems - Michael Wooldridge*
- [4]: https://direct.mit.edu/books/monograph/2503/Growing-Artificial-SocietiesSocial-Science-from
  *Livro no MIT Press: Growing Artificial Societies: Social Science from the Bottom Up (1996)*

<div> 
  <a href="https://www.youtube.com/@msjujubr" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" target="_blank"></a>
  <a href="https://instagram.com/msjujubr" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
 	<a href="https://www.twitch.tv/msjujubr" target="_blank"><img src="https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white" target="_blank"></a>
  <a href = "mailto:juliamourasouza10@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://www.linkedin.com/in/msjujubr/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
</div>
