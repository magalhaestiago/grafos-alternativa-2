def criar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0) # TENTAR ABORDAGEM linha[i][j]
        matriz.append(linha)
    return matriz

class Grafo:
    # Função construtora
    def __init__(self, qtdVertices):
        self.qtdVertices = qtdVertices
        self.qtdArestas = 0
        self.matrizAdjacencia = criar_matriz(self.qtdVertices)
        pass
    
    # Função para printar e visualizar matriz de adjacencia
    def mostrarMatriz(self, matriz):    
        for linha in matriz:
            for elemento in linha:
                print(elemento, end=" ")
            print()
            
    # Função para adicionar arestas entre dois vértices
    def adicionaAresta(self, u, v): # Grafo não direcionado!
        self.matrizAdjacencia[u-1][v-1] = 1
        self.matrizAdjacencia[v-1][u-1] = 1
        self.qtdArestas = self.qtdArestas + 1
        pass
    
    # a) Função que retorna a quantidade de vértices presentes no grafo
    def n(self):
        return self.qtdVertices 
        pass
    
    # b) Função que retorna a quantidade de arestas presentes no grafo
    def m(self):
        return self.qtdArestas
    
    # c) Função que retorna a vizinhança de um vértice v, ou seja, os vértices adjacentes a v
    def viz(self, vertice):
     
        linha = self.matrizAdjacencia[vertice - 1]
        
        adjacentes = []
        for i in range(self.qtdVertices):
            if linha[i] == 1:
                adjacentes.append(i + 1)
                
        return adjacentes

        
        pass
    
    # d) Função que retorna o grau de v, ou seja o número de arestas que incidem em v
    def d(self, vertice):
        
        linha = self.matrizAdjacencia[vertice - 1]
        cont = 0
        for i in range(self.qtdVertices):
            if linha[i] == 1:
                cont = cont + 1
                
        return cont
     
    # f) Retorna o menor grau presente no grafo
       
    def mind(self):
        menor = 10000
        
        for i in range(self.qtdVertices):
            aux = self.d(i)
            if aux < menor:
                menor = aux
                
        return menor
    
    # g) Retorna o maior grau presente no grafo
    
    def maxd(self):
        maior = 0
        
        for i in range(self.qtdVertices):
            aux = self.d(i)
            if aux > maior:
                maior = aux
                
        return maior
    
    

g = Grafo(4)
g.adicionaAresta(2,1)
g.adicionaAresta(3,1)
g.adicionaAresta(4,1)
# g.adicionaAresta(4,2)


g.mostrarMatriz(g.matrizAdjacencia)
print("Quantidade de vertices: ",g.n())
print("Quantidade de arestas: ",g.m())
#print(g.viz(1))
print(g.viz(3))
print(g.d(3))
print(g.mind())
print(g.maxd())



    
    
