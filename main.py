import matplotlib.pyplot as plt
import networkx as nx
import os

class Grafo:
    def __init__(self, vert):
        self.vert = vert #vert = vertice
        self.grafo = [[0]*self.vert for i in range(self.vert)]

    def adicionando_arestas(self, a, b, direcionado=False):
        if 1 <= a <= self.vert and 1 <= b <= self.vert and a != b:
            if direcionado:
                self.grafo[a-1][b-1]= 1 #direcionado
            else:
                self.grafo[a-1][b-1]= 1 
                self.grafo[b-1][a-1]= 1 #o grafo não direcionado
        else:
            print("Aresta inválida: ({}, {})".format(a, b))

    def visualizar_matriz(self):
        print('A matriz adjacência representada apartir do arquivo: \n')
        for i in range(self.vert):
            print(self.grafo[i])

    def visite_aresta(self):
        num_arestas = 0
        for i in range(self.vert):
            for j in range(i+1, self.vert):
                if self.grafo[i][j] == 1:
                    num_arestas+=1
        return num_arestas
    
    def vert_Adjcencia(self, vert1, vert2):
        verificador = 0
        if self.grafo[vert1-1][vert2-1]==1:
            verificador = 1
        return verificador
    
    def calcular_graus_vert(self, vert):
        contador_grau = 0
        for i in range(self.vert):
            if self.grafo[vert-1][i]==1:
                contador_grau += 1
        return contador_grau
    
    def calcular_vizinhos_vert(self, vert):
        lista_vizinhos = []
        for i in range(self.vert):
            if self.grafo[vert-1][i]==1:
                lista_vizinhos.append(i+1)
        return lista_vizinhos
    
    def VerificarCiclos(self):
        def busca_profundidade(vertice, visitados, pilha):
            visitados.add(vertice)
            pilha.add(vertice)
            for vizinho in range(self.vert):
                if self.grafo[vertice][vizinho] == 1:
                    if vizinho in pilha:
                        return True
                    elif vizinho not in visitados and busca_profundidade(vizinho, visitados, pilha):
                        return False
            pilha.remove(vertice)
            return False

        for vertice in range(self.vert):
            visitados = set()
            pilha = set()
            if busca_profundidade(vertice, visitados, pilha):
                return True
        return False
    
    def VerificarArvore(self):
        if self.visite_aresta() != self.vert - 1:
            return False
        
        visitados = set()
        pilha = [0] 
        while pilha:
            vertice = pilha.pop()
            if vertice not in visitados:
                visitados.add(vertice)
                for vizinho in range(self.vert):
                    if self.grafo[vertice][vizinho] == 1:
                        pilha.append(vizinho)
        
        # Se todos os vértices foram visitados, o grafo é conexo
        if len(visitados) != self.vert:
            return False
        
        # Verifica se o grafo não contém ciclos
        return not self.VerificarCiclos()
    
    def criar_lista_adjacencia(self):
        lista_adj = {i + 1: [] for i in range(self.vert)}
        for i in range(self.vert):
            for j in range(self.vert):
                if self.grafo[i][j] == 1:
                    lista_adj[i + 1].append(j + 1)
        return lista_adj

    def salvar_lista_adjacencia(self, arquivo):
        lista_adj = self.criar_lista_adjacencia()
        with open(arquivo, 'w') as f:
            for vertice in lista_adj:
                linha = f"{vertice}: " + ", ".join(map(str, lista_adj[vertice])) + "\n"
                f.write(linha)

def visualize_grafo(arquivo_lista_adj):
    g = nx.Graph()
    with open(arquivo_lista_adj, 'r') as file:
        for line in file:
            vertice, adjacencias = line.strip().split(':')
            vertice = int(vertice)
            adjacencias = list(map(int, adjacencias.split(',')))
            for adj in adjacencias:
                g.add_edge(vertice, adj)
    nx.draw(g, with_labels=True)
    plt.show()


def criar_grafo_de_arquivo(arquivo, numV):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    Ndirecionado = linhas[0].strip().lower() == 'ND'

    grafo = Grafo(numV)

    for linha in linhas[1:]:
        v1, v2 = map(int, linha.split(","))
        grafo.adicionando_arestas(v1, v2, False)
        if not Ndirecionado:
            grafo.adicionando_arestas(v2, v1, True)
    return grafo

nome_arquivo = "grafoDigitado.txt"
numVe= int(input("Digite a quantidade de vértices no grafo: "))
meu_grafo = criar_grafo_de_arquivo(nome_arquivo, numVe)
meu_grafo.visualizar_matriz()


def menu():
    print("\n\n-------------MENU---------------")
    print("\n1 - VERIFICAR SE 2 VÉRTICES SÃO ADJACENTES")
    print("\n2 - VERIFICAR TODAS AS ARESTAS")
    print("\n3 - CALCULAR O GRAU DE VÉRTICE QUALQUER")
    print("\n4 - BUSCAR VIZINHOS DE UM VÉRTICE")
    print("\n5 - VERIFICAR SE HÁ CICLOS NO GRAFO(BFS)")
    print("\n6 - VERIFICAR SE É UMA ÁRVORE NO GRAFO(BFS)")
    print("\n7 - VISUALIZAR GRAFO(NOVO ARQUIVO .TXT)")
    print("\n8 - FECHAR PROGRAMA")
    print("\n--------------------------------------")

def visitar_todas_arestas():
    print("\nA quantidade de arestas presente no grafo é: ", meu_grafo.visite_aresta())
    
    
def verificar_grau_vertices():
    cont2=0
    while(cont2==0):
        print("\n---------------------------------------------------------------------------")
        print("\nCalcular o grau de um vértice qualquer\n")
        vert_teste = int(input("Digite o número do vértice a ser calculado seu grau: "))
        numVert_grau = meu_grafo.calcular_graus_vert(vert_teste)
        print(f"\nO grau do vértice {vert_teste} é: ", numVert_grau)
        verificandoOp = input("\n\nDeseja verificar outros vértices[s/n]: ")
        if(verificandoOp=='s'):
            continue
        else:
            break

# Função para ler o arquivo de texto e criar o grafo
"""def criar_grafo_lista_adjacencia(file_path):
    g = nx.Graph()  # Usando nx.Graph() para um grafo não direcionado
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            # Separando o nó principal dos seus nós adjacentes
            node, adj_nodes = line.strip().split(':')
            node = int(node.strip())
            adj_nodes = [int(adj_node.strip()) for adj_node in adj_nodes.split(',') if adj_node.strip()]
            for adj_node in adj_nodes:
                g.add_edge(node, adj_node)
    return g

# Função para visualizar o grafo
def visualize_grafo(grafo):
    nx.draw(grafo, with_labels=True)
    plt.show()"""


contador = 0
while (contador==0):
    os.system("cls")
    meu_grafo.visualizar_matriz()
    menu()
    valor = int(input("\nDigite a opção a ser escolhida: "))
    os.system("cls")
    match valor:
        case 1:
            os.system("cls")
            continuar = 0
            while(continuar==0):
                meu_grafo.visualizar_matriz()
                print("\n---------------------------------------------------------------------------")
                print("\nVerificar se vértices são adjacentes\n")
                vert1 = int(input("Digite o número do vértice 1: "))
                vert2 = int(input("\nDigite o número do vértice 2: "))
                verificador = meu_grafo.vert_Adjcencia(vert1, vert2)
                if verificador == 1:
                    print("\n---------------------------------------------")
                    print(f"\nOs vértices {vert1} e {vert2} são adjacentes")
                else:
                 print("\n---------------------------------------------")
                 print("\nOs vértices não são adjacentes")
                
                verificador2 = input("\nDeseja verificar outros vértices[s/n]: ")
                if(verificador2=='s'):
                    os.system("cls")
                    continue
                else:
                    break

            
        case 2:
            os.system("cls")
            meu_grafo.visualizar_matriz()
            visitar_todas_arestas()
            resposta = input("\nDigite 's' para retornar: ")
            if resposta=='s':
                continue
            
        case 3:
            os.system("cls")
            meu_grafo.visualizar_matriz()
            verificar_grau_vertices()
        
        case 4:
            os.system("cls")
            meu_grafo.visualizar_matriz()
            verificar_continuar = 0
            while(verificar_continuar==0):
                os.system("cls")
                meu_grafo.visualizar_matriz()
                numVert = int(input("\nDigite o número do vértice a buscar seus vizinhos: "))
                listaVert = meu_grafo.calcular_vizinhos_vert(numVert)
                print(f"\nOs vizinhos de {numVert} são: ", listaVert[0:] )
                verificador_2 = input("\nDeseja verificar outros vértices[s/n]: ")
                if(verificador_2=='s'):
                    continue
                else:
                    break

        case 5:
            os.system("cls")
            meu_grafo.visualizar_matriz()
            if meu_grafo.VerificarCiclos()==True:
                print("\n----------------------------")
                print("\nHÁ CICLOS DENTRO DO GRAFO")
                print("\n----------------------------")
            else:
                print("\n----------------------------")
                print("\nO GRAFO NÃO CONTÉM CICLOS")
                print("\n----------------------------")
            
            resposta2 = input("\nDigite 's' para retornar: ")
            if resposta2=='s':
                continue
        case 6:
            os.system("cls")
            meu_grafo.visualizar_matriz()
            if meu_grafo.VerificarArvore()==True:
                print("\n----------------------------")
                print("\nHÁ PRESENÇA DE UMA ÁRVORE NO GRAFO")
                print("\n----------------------------")
            else:
                print("\n----------------------------")
                print("\nNÃO HÁ UMA ÁRVORE PRESENTE NO GRAFO")
                print("\n----------------------------")
            
            resposta2 = input("\nDigite 's' para retornar: ")
            if resposta2=='s':
                continue
        
        case 7:
            lista_adj_arquivo = "lista_adj.txt"
            meu_grafo.salvar_lista_adjacencia(lista_adj_arquivo)
            print(f"\nLista de adjacência salva no arquivo: {lista_adj_arquivo}")

            print("\nVisualizando o grafo:")
            visualize_grafo(lista_adj_arquivo)
        case 8:
            print("------FECHANDO ALGORITMO--------")
            break
        case _:
            print("Número digitado inválido!!")
            continue

