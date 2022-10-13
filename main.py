
from noh import *

class FilaVazia(Exception):
  pass

class Fila:
  def __init__(self):
    self._dados = Noh()
    self._tamanho = 0
    self._inicio = 0
    self.head = None

  def __len__(self):
    return self._tamanho

  def isEmpty(self):
    return self._tamanho == 0

  def first(self):
    if self.isEmpty():
      raise FilaVazia('\nA Fila está vazia')
    return self.head.getData()

  def dequeue(self):
    if self.isEmpty():
      print('\nA Fila está vazia')
    else:
      elementoAtual = self._dados
      proximoElemento = elementoAtual.getNext()
      self._dados = proximoElemento
      self.head = proximoElemento
      
      self._tamanho -= 1
      return elementoAtual

  def enqueue(self, e):
    temp = self._dados
    while True:
      if (self._tamanho == 0):
        self._dados = Noh(e)
        self.head = self._dados
        break
      else:
        if (temp.getNext() == None):
          noh = Noh(e)
          temp.setNext(noh)
          break
        else:
          temp = temp.getNext()

    self._tamanho += 1                        

  def girarFila(self, quantidade):
    if self.isEmpty():
      print('\nNão há candidatos para girar')
    else:
      quant = quantidade % self._tamanho
      cont = 1
      while cont <= quant:
        elementoRemovido = self.dequeue()
        self.enqueue(elementoRemovido.getData())
        cont += 1
      
  def mostrar(self):
    if self.isEmpty():
      return '\nNão há candidatos para mostrar'
    else:
      lista = []
      temp = self._dados
      while (True):
        lista.append(temp.getData())
        if (temp.getNext() == None):
          break
        temp = temp.getNext()
      
      return lista
