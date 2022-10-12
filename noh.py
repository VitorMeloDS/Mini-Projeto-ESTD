from fila import Noh
from noh import *

class FilaVazia(Exception):
    pass

class Fila:
  def __init__(self, capacidade):
    self._dados = Noh()
    self._tamanho = 0
    self._inicio = 0

  def __len__(self):
    return self._tamanho

  def isEmpty(self):
    return self._tamanho == 0

  def first(self):
    if self.isEmpty():
      raise FilaVazia('\nA Fila está vazia')
    return self._dados.head.getData()

  def dequeue(self):
    if self.isEmpty():
      raise FilaVazia('\nA Fila está vazia')
    
    elementoAtual = self._dados.head
    proximoElemento = self._dados.head.getNext()
    self._dados.head = proximoElemento
    
    self._tamanho -= 1
    return elementoAtual.getData()

  def enqueue(self, e):
    temp = self._dados
    while (True):
      if (temp.getNext() == None):
        break
      temp = self.dados.getNext()
    self._dados.setData(e)
    if (self.tamanho == 0):
      self._dados.head = e

    temp.setNext(e)
    self._tamanho += 1                        

  def girarFila(self, quantidade):
    if self.isEmpty():
        print('\nNão há candidatos para girar')
    else:
        cont = 1
        while cont <= quantidade:
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
        temp = self.dados.getNext()
      
      return lista
