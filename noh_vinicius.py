class Noh:
  def __init__(self, valor_inicial):
    self._dados = valor_inicial
    self.head = None
    
  def getData(self):
      return self._dados
    
  def getNext(self):
    return self.head
  
  def setData(self, novo_valor):
    self._dados = novo_valor
    
  def setNext(self, novo_proximo):
    self.head = novo_proximo
