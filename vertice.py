from aresta import Aresta
class Vertice:
  def __init__(self, id) -> None:
    self.id = id
    self.saturado = None
    self.arestas = {}

  def ehSaturado(self):
    return self.saturado

  def setSaturacao(self, saturado):
    self.saturado = saturado

  def incluiVizinho(self, aresta, idVizinho):
    self.arestas[idVizinho] = aresta
  
  def getVizinhos(self):
    vizinhos = []
    for a in self.arestas.values():
      if self.id == a.v1.id:
        vizinhos.append(a.v2)
      else:
        vizinhos.append(a.v1)
    return vizinhos
  
  def __repr__(self):
    if self.saturado:
      return f"[{self.id}]>{self.saturado.id}"
    return f"[{self.id}]>None"
  