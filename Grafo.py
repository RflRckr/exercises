import random


class Vertice(object):
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

# grafo lista de adjacência


class Grafo:
    def __init__(self, dic_grafo=None):
        if dic_grafo is None:
            self.listaDeVertices = {}
        else:
            self.listaDeVertices = dic_grafo

    def __toString__(self):
        string = ''
        for key, value in self.listaDeVertices.items():
            string += str(value)
        if not string:
            string = '(Empty)'
        return string

    def adiciona_vertice(self, vertice):
        if vertice in self:
            print('Vértice %s já existe!\n' % vertice)
            return False
        self.listaDeVertices[vertice] = Vertice(vertice)
        print('Vértice %s adicionado ao grafo' % vertice)
        return True

    def remove_vertice(self, vertice):
        if vertice not in self:
            print('Vértice %s não existe!\n' % vertice)
            return False
        removido = self.listaDeVertices.pop(vertice)
        for key, vertice in self.listaDeVertices.items():
            if removido in vertice.proximo:
                vertice.vizinhos.remove(removido)
        return True

    def conecta(self, v1, v2):
        if v1 not in self:
            print('Vértice %s não existe!\n' % v1)
            return False
        if v2 not in self:
            print('Vértice %s não existe!\n' % v2)
            return False
        self.listaDeVertices[v1].vizinhos.append(self.listaDeVertices[v2])
        self.listaDeVertices[v2].vizinhos.append(self.listaDeVertices[v1])
        print('Aresta %s conectada com aresta %s!\n' % (v1, v2))
        return True

    def desconecta(self, v1, v2):
        if v1 not in self:
            print('Vértice %s não existe!\n' % v1)
            return False
        if v2 not in self:
            print('Vértice %s não existe!\n' % v2)
            return False
        if self.listaDeVertices[v2] in self.listaDeVertices[v1].proximo:
            self.listaDeVertices[v1].vizinhos.remove(self.listaDeVertices[v2])
            self.listaDeVertices[v2].vizinhos.remove(self.listaDeVertices[v1])
        else:
            print('Aresta %s não está conectada a aresta %s!\n' % (v1, v2))
        return True

    def ordem(self):
        return len(self.listaDeVertices.keys())

    def vertices(self):
        return list(self.listaDeVertices.keys())

    def um_vertice(self):
        return random.choice(self.listaDeVertices.keys())

    def adjacentes(self, vertice):
        if vertice not in self:
            print('Vértice %s não existe!\n' % vertice)
            return False
        else:
            return self.listaDeVertices[vertice].vizinhos

    def grau(self, vertice):
        if vertice not in self:
            print('Vértice %s não existe!\n' % vertice)
            return False
        else:
            return len(self.listaDeVertices[vertice].vizinhos)

# Verifica se todos os vértices do grafo possuem o mesmo grau
    def __eh_regular__(self):
        n = self.grau(self.um_vertice())
        for key, vertice in self.listaDeVertices.keys():
            if vertice.__grau__(vertice) != n:
                return False
        return True

# Verifica se cada um dos vértices do grafo estão conectados a todos os outros vértices
    def __eh_completo__(self):
        n = ((self.ordem()) - 1)
        for key, vertice in self.listaDeVertices.keys():
            if vertice.__grau__(vertice) != n:
                return False
        return True

# Retorna um conjunto contendo todos os vértices do grafo que são transitivamente alcançáveis partindo-se de v
    def fecho_transitivo(self, v):
        novo_dict = []
        return self.__procura_fecho_transitivo__(v, novo_dict)

# Método privado utilizado pelo método fech_transitivo
    def __procura_fecho_transitivo__(self, v, visitados):
        visitados.append(v)
        for key, vertice in self.adjacentes(v):
            if vertice not in visitados:
                self.__procura_fecho_transitivo__(vertice, visitados)
        return visitados

# Verifica se existe pelo menos um caminho entre cada par de vértices
    def eh_conexo(self):
        a = self.vertices()
        b = (self.fecho_transitivo(self.um_vertice()))
        if ((a>b) - (a<b)) == 0:
            return True
        else:
            return False

# Verifica se o grafo é uma árvore, ou seja, se não possue ciclos e se é conexo
    def eh_arvore(self):
        v = self.um_vertice()
        novo_dict = []
        if ((self.eh_conexo()) == True) and (self.__ha_ciclo_com(v, v, novo_dict) == False):
            return True
        else:
            return False

# Método privado utilizado pelo método eh_arvore para verificar se v faz parte de algum ciclo no grafo
    def __ha_ciclo_com(self, v, v_anterior, visitados):
        if v in visitados:
            return True
        visitados.append(v)
        for key, vertice in self.adjacentes(v):
            if vertice != v_anterior:
                if self.__ha_ciclo_com(vertice, v, visitados):
                    return True
        visitados.remove(v)
        return False

if __name__ == "__main__":
    g = {
        "a": ["d"],
        "b": ["c"],
        "c": ["b", "c", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": []
    }

    grafo = Grafo(g)

    print("Vértices do grafo: \n")
    print(grafo.vertices())
