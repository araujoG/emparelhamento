class Aresta:
  def __init__(self, v1, v2) -> None:
    self.v1 = v1
    self.v2 = v2
  
  def __repr__(self):
    return f"[{self.v1.id}--{self.v2.id}]"