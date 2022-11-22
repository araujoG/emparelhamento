import random
from aresta import Aresta;
from vertice import Vertice;

class Grafo:
  def __init__(self) -> None:
    self.vertices = []
    self.entrada = [[1,2,3,4,5],
                    [1,2,3,4,5],
                    [1,2,3,4,5]]
    self.cardinalidadeX = len(self.entrada)
    self.cardinalidadeY = len(self.entrada[0])

  # Inicializa o grafo pela matriz de entrada
  def inicializaGrafo(self):
    for i in self.cardinalidadeX:
      self.vertices.append(Vertice(f"X{i}"))
    for j in self.cardinalidadeY:
      self.vertices.append(Vertice(f"Y{j}"))

    for i in self.cardinalidadeX:
      for j in self.cardinalidadeY:
        self.incluiVizinhanca(f"X{i}", f"Y{j}", self.entrada[i][j])

  # Inclui uma aresta bidirecional
  def incluiVizinhanca(self, v1, v2, custo):
    vertice1 = self.getVertice(v1)
    vertice2 = self.getVertice(v2)
    if vertice1 != None and vertice2 != None:
      vertice1.incluiVizinho(v2, custo)
      vertice2.incluiVizinho(v1, custo)
  
  # Retornar o vértices através do id
  def getVertice(self, id):
    for vertice in self.vertices:
      if vertice.id == id:
        return vertice;
    return None

  # Retornar todos os vértices não saturados do grafo
  def getVerticesInsaturados(self):
    insaturados = []
    for vertice in self.vertices:
      if not vertice.saturado:
        insaturados.append(vertice)
    return insaturados;

  # Retornar um caminho M-aumentante
  def caminhoAumentante(self):
    pass