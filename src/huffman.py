import heapq
import json
from collections import Counter


# Definição do Nó de Huffman
class NoHuffman:
    def __init__(self, simbolo, freq):
        self.simbolo = simbolo    # palavra
        self.freq = freq          # frequência da palavra
        self.esquerda = None      # filho esquerdo
        self.direita = None       # filho direito

    # Permite comparar nós dentro da heap
    def __lt__(self, outro):
        # Para garantir ordenação quando frequências são iguais
        if self.freq == outro.freq:
            # Ordena por símbolo em ordem alfabética
            return str(self.simbolo) < str(outro.simbolo)
        return self.freq < outro.freq


# Função para construir a árvore de Huffman
# Recebe um dicionário {palavra: frequência}, retorna o nó raiz da árvore
def construir_arvore(frequencias):
    
    heap = [NoHuffman(simbolo, freq) for simbolo, freq in frequencias.items()]
    heapq.heapify(heap)  # transforma a fila em uma min-heap

    # Enquanto houver mais de um nó, combinamos os dois de menor frequência
    while len(heap) > 1:
        no1 = heapq.heappop(heap)
        no2 = heapq.heappop(heap)
        novo_no = NoHuffman(None, no1.freq + no2.freq)
        novo_no.esquerda = no1
        novo_no.direita = no2
        heapq.heappush(heap, novo_no)

    return heap[0]


# Geração dos códigos de Huffman recursivamente
def gerar_codigos(no, codigo_atual="", codigos=None):
    if codigos is None:
        codigos = {}

    # Se for folha, adiciona o código gerado
    if no.simbolo is not None:
        codigos[no.simbolo] = codigo_atual
        return codigos

    # Caminha para a esquerda -> adiciona '0'
    if no.esquerda:
        gerar_codigos(no.esquerda, codigo_atual + "0", codigos)

    # Caminha para a direita -> adiciona '1'
    if no.direita:
        gerar_codigos(no.direita, codigo_atual + "1", codigos)

    return codigos


# Compressão do texto com base nos códigos
def comprimir_texto(texto, codigos):
    palavras = texto.split()
    texto_codificado = ''.join(codigos[p] for p in palavras)
    return texto_codificado


# Descompressão do texto codificado usando a árvore de Huffman
def descomprimir_texto(texto_codificado, raiz):
    resultado = []
    no_atual = raiz
    for bit in texto_codificado:
        if bit == '0':
            no_atual = no_atual.esquerda
        else:
            no_atual = no_atual.direita

        # Se chegar a uma folha, adiciona o símbolo ao resultado
        if no_atual.simbolo is not None:
            resultado.append(no_atual.simbolo)
            no_atual = raiz  # volta para a raiz

    return ' '.join(resultado)

# Função para serializar a árvore
def serializar_arvore(no):
    if no.simbolo is not None:
        return {'simbolo': no.simbolo}
    return {
        'esquerda': serializar_arvore(no.esquerda),
        'direita': serializar_arvore(no.direita)
    }


def main():
    # Lê o conteúdo do arquivo input.dat
    try:
        with open("data/input.dat", "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
    except FileNotFoundError:
        print("Arquivo de entrada não encontrado")
        return
 
    # Divide o conteúdo em textos separados por linhas vazias
    textos = [t.strip() for t in conteudo.split("\n") if t.strip()]
    resultados = [] 

    # Processamento de cada texto individualmente
    for i, texto in enumerate(textos, 1):
        # Divide o texto em palavras (separadas por espaços)
        palavras = texto.split()
        
        # Conta a frequência de cada palavra
        frequencias = Counter(palavras)
        
        # Constrói a árvore de Huffman
        raiz = construir_arvore(frequencias)
        
        # Gera códigos binários
        codigos = gerar_codigos(raiz)
        
        # Comprime o texto
        texto_comprimido = comprimir_texto(texto, codigos)

        # Serializa a estrutura da árvore de Huffman
        arvore_serializada = serializar_arvore(raiz)

        # Armazena os dados
        resultados.append({
            "texto_original": texto,
            "frequencias": dict(frequencias),
            "arvore_huffman": arvore_serializada,
            "codigos": codigos,
            "texto_comprimido": texto_comprimido,
            "Tamanho comprimido": f"{len(texto_comprimido)} bits",
            "numero_palavras": len(palavras),
            "palavras_unicas": len(codigos)
        })
 

    # Salva os resultados em output.dat
    with open("data/output.dat", "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)

    print("\nCompressão concluída! Resultados salvos em 'output.dat'.")


if __name__ == "__main__":
    main()
