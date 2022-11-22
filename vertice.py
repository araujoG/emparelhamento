from aresta import Aresta
class Vertice:
  def __init__(self, id) -> None:
    self.id = id
    self.saturado = False
    self.cor = False
    self.arestas = []

  def ehSaturado(self):
    return self.saturado

  def setSaturacao(self, saturado):
    self.saturado = saturado

  def incluiVizinho(self, idVizinho, custo):
    self.arestas.append(Aresta(self.id, idVizinho, custo))