import random
from aresta import Aresta;
from vertice import Vertice;

class Grafo:
  def __init__(self) -> None:
    self.vertices = []
    self.entrada = [[1,1,0,0],
                    [0,1,1,0],
                    [0,1,1,0],
                    [0,0,0,0]]
    self.cardinalidadeX = len(self.entrada)
    self.cardinalidadeY = len(self.entrada[0])
    self.emparelhamento = []
    self.inicializaGrafo()

  # Inicializa o grafo pela matriz de entrada
  def inicializaGrafo(self):
    verticesX = []
    verticesY = []
    for i in range(self.cardinalidadeX):
      verticesX.append(Vertice(f"X{i}"))
    for j in range(self.cardinalidadeY):
      verticesY.append(Vertice(f"Y{j}"))
    self.vertices.append(verticesX)
    self.vertices.append(verticesY)

    for i in range(self.cardinalidadeX):
      for j in range(self.cardinalidadeY):
        existe = self.entrada[i][j]
        if (existe):
          self.incluiVizinhanca(verticesX[i], verticesY[j])

  # Inclui uma aresta bidirecional
  def incluiVizinhanca(self, v1, v2):
    a = Aresta(v1,v2)
    v1.incluiVizinho(a, v2.id)
    v2.incluiVizinho(a, v1.id)

  # Retornar todos os vértices não saturados do grafo
  def getVerticesInsaturados(self):
    insaturados = []
    for vertice in self.vertices:
      if not vertice.saturado:
        insaturados.append(vertice)
    return insaturados

  # Retornar um caminho M-aumentante
  def caminhoAumentante(self, vInsaturado):
    verticesVisitados = [vInsaturado]
    vizinhosVisitados = []
    vizinhos = vInsaturado.getVizinhos()
    caminhos = [[vInsaturado]]
    while not all(item in vizinhosVisitados for item in vizinhos):
      pai, vizinho = getVizinho(vizinhos, vizinhosVisitados, verticesVisitados)
      if vizinho.saturado:
        caminhos = adicionaCaminho(caminhos,pai,vizinho)
        verticesVisitados.append(vizinho.saturado)
        vizinhosVisitados.append(vizinho)
        vizinhos.extend(vizinho.saturado.getVizinhos())
      else:
        caminhos = adicionaCaminho(caminhos,pai,vizinho)
        return getBordas(caminhoAtual(caminhos,vizinho))
    return []

  def emparelha(self):
    if self.ehEmparelhamentoPerfeito():
      return self.emparelhamento
    while(True):
      naoSaturados = getNaoSaturados(self.getMenorParticicao())
      if(naoSaturados == []):
          break 
      u = naoSaturados[0]
      caminho = self.caminhoAumentante(u)
      if(caminho == []):
          break 
      self.difSimetrica(caminho)
      
    pass

  def ehEmparelhamentoPerfeito(self):
    if len(self.emparelhamento) == self.cardinalidadeX or len(self.emparelhamento) == self.cardinalidadeY:
      return True
    return False
  
  def difSimetrica(self, caminho):
    novoEmparelhamento = []
    for aresta in self.emparelhamento:
      if aresta not in caminho:
        novoEmparelhamento.append(aresta)
        aresta.v1.saturado = aresta.v2
        aresta.v2.saturado = aresta.v1
      else:
        aresta.v1.saturado = None
        aresta.v2.saturado = None
    for aresta in caminho:
      if aresta not in self.emparelhamento:
        novoEmparelhamento.append(aresta)
        aresta.v1.saturado = aresta.v2
        aresta.v2.saturado = aresta.v1
   
    self.emparelhamento = novoEmparelhamento

  def getMenorParticicao(self):
    if self.cardinalidadeX < self.cardinalidadeY:
      return self.vertices[0]
    return self.vertices[1]

def adicionaCaminho(caminhos, pai, vizinho):
  ultimoNivel = []
  for caminho in caminhos:
    if pai in caminho:
      ultimoNivel = caminho
      if caminho[-1] == pai:
        caminho.append(vizinho)
        if vizinho.saturado:
          caminho.append(vizinho.saturado)
        return caminhos
  novoCaminho = []
  for i in ultimoNivel:
    if i == pai:
      novoCaminho.append(pai)
      novoCaminho.append(vizinho)
      caminhos.append(novoCaminho)
      if vizinho.saturado:
        caminho.append(vizinho.saturado)
      return caminhos
    else:
      novoCaminho.append(i)
      
def caminhoAtual(caminhos, vertice):
  for caminho in caminhos:
    if vertice in caminho:
      return caminho

def getVizinho(vizinhos,vizinhosVisitados, verticesVisitados):
  for vizinho in vizinhos:
    if vizinho not in vizinhosVisitados:
      for pai in vizinho.getVizinhos():
        if pai in verticesVisitados:
          return pai, vizinho

def getNaoSaturados(vertices):
  naoSaturados = []
  for v in vertices:
    if not v.saturado:
      naoSaturados.append(v)
  return naoSaturados

def getBordas(caminho):
  bordas = []
  for i in range(1, len(caminho)):
    bordas.append(caminho[i-1].arestas[caminho[i].id])
  return bordas