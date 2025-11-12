# Implementação do Código de Huffman

# Simulação de Incêncio com Movimentação de um Animal
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
O algoritmo de Huffman foi desenvolvido por David A. Huffman em 1952, como parte de sua pesquisa de doutorado na Universidade de MIT. Ele surgiu como uma solução eficiente para compressão de dados sem perdas, buscando reduzir o espaço necessário para armazenar informações, aproveitando a frequência de ocorrência de símbolos em uma mensagem. A ideia central era representar símbolos mais comuns com códigos binários mais curtos e símbolos menos frequentes com códigos mais longos, otimizando o uso do espaço de armazenamento.

O princípio básico do algoritmo de Huffman é a codificação de prefixo, que garante que nenhum código atribuído a um símbolo seja prefixo de outro. Isso evita ambiguidades na decodificação. A eficiência do método se baseia em analisar a frequência de cada símbolo no conjunto de dados e construir uma representação binária que minimize o número total de bits necessários para codificar a mensagem completa.

Neste trabalho, apresento uma aplicação em linguagem Python do algoritmo, capaz de realizar a compressão de pequenos trechos de texto utilizando o código de Huffman como método.

## O Algoritmo
### Construção da Árvore Huffman
### Geração dos Códigos Binários

## Compilação, Entradas e Saídas
### Input.dat
### Output.dat

    Struct Config{
    // Variáveis Personalizáveis
    int iteracoes = 100;
    bool vntD = 0, vntE = 0, vntC = 0, vntB = 0;

    // Variáveis Globais
    std::vector<std::vector<int>> floresta;
    std::vector<std::pair<int, int>> arv_1_2, arv_2_3;
    int n, m, animX, animY, animMov, animCnt, animMrt;
    bool animVid;
    };

| Função            | Descrição                                                  |
|-------------------|------------------------------------------------------------|
| [`bool atividade_fogo()`](https://github.com/msjujubr/Atividade01/blob/main/src/config.cpp#L260)  | Retorna true (1) caso ainda há árvores para serem queimadas.  |
| [`void configuracoes()`](https://github.com/msjujubr/Atividade01/blob/main/src/config.cpp#L28) | Processa o arquivo Input.dat e armazena as informações nas variáveis globais; Inicializa o animal |
| [`int defVento()`](https://github.com/msjujubr/Atividade01/blob/main/src/config.cpp#L8)     | Retorna um número de acordo com o caso de vento (tabela abaixo) |
| [`void inicio_animal()`](https://github.com/msjujubr/Atividade01/blob/main/src/config.cpp#L265)    | Inicializa as variáveis do animal; Gera uma coordenada aleatória entre os 0 e 1 disponíveis na matriz para ser a posição inicial do animal na simulação |
| [`void prop(int x, int y, vector<pair<int,int>>& auxiliar)`](https://github.com/msjujubr/Atividade01/blob/main/src/config.cpp#L286) | Confere se na posição (x, y) tem uma árvore saudável (1), se caso afirmativo, queima (2) e armazena no vetor |
| [`void propagacao()`](https://github.com/msjujubr/Atividade01/blob/main/src/config.cpp#L67)     | Espalha o fogo de acordo com o caso de vento; Para todas as árvores que queimaram na iteração anterior (arv_1_2), pega os vizinhos possíveis e chama a função prop() para cada um; As árvores em arv_1_2 vão para o vetor arv_2_3 e as novas árvores queimadas são armazenadas em arv_1_2. |
| [`void queimada()`](https://github.com/msjujubr/Atividade01/blob/main/src/config.cpp#L295)  | Define como queimadas (3) todas as árvores do vetor arv_2_3 |
| [`void salvar()`](https://github.com/msjujubr/Atividade01/blob/main/src/config.cpp#L241)    |  Salva a matriz e as coordenadas do animal |
| [`void relatorio()`](https://github.com/msjujubr/Atividade01/blob/main/src/config.cpp#L249) | Salva a quantidade de passos do animal e o estado dele ao final do programa |

<div align="center"> <table> <tr> <td>

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
