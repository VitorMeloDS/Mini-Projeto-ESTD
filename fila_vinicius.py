from noh import *

class FilaVazia(Exception):
    pass

class Fila:
  def __init__(self, capacidade):
    self._dados = [None] * capacidade
    self._tamanho = 0
    self._inicio = 0
    self.head = None

  def __len__(self):
    return self._tamanho

  def isEmpty(self):
    return self._tamanho == 0

  def first(self):
    if self.isEmpty():
      raise FilaVazia('A Fila está vazia')
    return self._dados[self._inicio].getData()

  def dequeue(self):
    if self.isEmpty():
      raise FilaVazia('A Fila está vazia')
    result = self._dados[self._inicio]
    self._dados[self._inicio] = None
    self._inicio = (self._inicio + 1) % len(self._dados)
    self._tamanho -= 1
    return result

  def enqueue(self, e): 
    if self._tamanho == len(self._dados):
      self.altera_tamanho(2 * len(self._dados))
    disponivel = (self._inicio + self._tamanho) % len(self._dados)
    temp = Noh(e)
    temp.setNext(self.head)
    self.head = temp
    self._dados[disponivel] = temp
    self._tamanho += 1

  def altera_tamanho(self, novo_tamanho):   
    dados_antigos = self._dados              
    self._dados = [None] * novo_tamanho       
    posicao = self._inicio
    for k in range(self._tamanho):            
      self._dados[k] = dados_antigos[posicao] 
      posicao = (1 + posicao) % len(dados_antigos) 
    self._inicio = 0                          

  def girarFila(self, quantidade):
    if self.isEmpty():
        print('Não há candidatos para girar')
    else:
        cont = 1
        while cont <= quantidade:
            elementoRemovido = self.dequeue()
            self.enqueue(elementoRemovido.getData())
            cont += 1
      
  def mostrar(self):
    if self.isEmpty():
        return 'Não há candidatos para mostrar'
    else:
        info = ''
        for e in self._dados:
            if e != None:
                info += e.getData() + ' '

        info = info.replace(' ', ', ')
        info = list(info)
        del info[-1]
        del info[-1]
        info = ''.join(info)
        info = '[' + info + ']'

        return info
    
