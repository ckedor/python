#Fila de prioridades com Binary Heap

#inserção: O(logN)
#remoção: O(logN)

#Max-Heap - Pais tem valor maior que os filhos
#Min-Heap - Pais tem valor menor que os filhos
#Pode ser implementada com vetor. Os filhos são acessados por:
#filhos à esquerda: 2i + 1
#filhos à direita: 2i + 2

import heapq

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __repr__(self):
        return 'Nome: %s' %self.nome
    
class FilaDePrioridade:
    
    def __init__(self):
        self.fila[]
        self._indice = 0
    
    def inserir(self, item, prioridade):
        heapq.heappush(self._fila, (-prioridade, self._indice, item))
        self._indice += 1
    
    def remove(self):
        return heappq.heappop(self._fila)[-1]
    
fila = FilaDePrioridade()
fila.inserir(Pessoa("Maria"), 20)
fila.inserir(Pessoa("Pedro"), 16)
fila.inserir(Pessoa("Felipe"), 80)
fila.inserir(Pessoa("Carol"), 23)

print(fila.remover())

