from typing import NoReturn
from fila import *
from os import system, name, _exit
from time import sleep


if __name__ == '__main__':
  candidatos = Fila(10)

  clear = lambda: system('cls' if name == 'nt' else 'clear')
  clear()

  def apresentacao() -> bool:
    inicializador = input('\nPara iniciar o processo digite "start", para buscar por algum candidato digite "search", para ver o primeiro candidato digite "first",\npara remover o primeiro candidato digite "remove",  para ver todos os candidatos digite "find all", para girar a fila digite "spin"\ne para sair digite "exit": ').lower().strip()

    if inicializador == 'start':
      return True
    elif inicializador == 'search':
      print('\nNão há candidatos para procurar!'); sleep(3); clear(); apresentacao()
      return True
    elif inicializador == 'find all':
      print('\nNão há candidatos para mostrar!'); sleep(3); clear(); apresentacao()
      return True
    elif inicializador == 'remove first':
      print('\nNão há candidatos para remover!'); sleep(3); clear(); apresentacao()
      return True
    elif inicializador == 'spin':
      print('\nNão há candidatos para girar!'); sleep(3); clear(); apresentacao()
      return True
    elif inicializador == 'first':
        print('\nNão há candidatos para mostrar!'); sleep(3); clear(); apresentacao()
        return True
    elif inicializador == 'exit':
      return False
    else:
      print('\nComando não reconhecido, digite uns dos comando expecificados!'); sleep(3); clear(); apresentacao()
      return True

  def addCandidato(novoCandidato):
    #candidatos.setData(novoCandidato)
    candidatos.enqueue(novoCandidato)
    print('Candidato cadastrado!')

  def findAll():
    print(candidatos.mostrar())
  
  def spin(numGiros = 1):
    candidatos.girarFila(numGiros)
    
  def first():
    print(candidatos.first())
    
  def remove():
    candidatos.dequeue()

  def entradaDado():
    try:
      while True:
        print('\nGerência de Candidatos Aprovados em Concurso Público.')
        candidato = input('\nInfome o nome do candidato: ').lower().strip()
        if candidato == 'exit':
          _exit(0)
        elif candidato == 'search':
          ...
        elif candidato == 'find all':
          print('\n')
          findAll()
          ...
        elif candidato == 'remove':
          remove()
        elif 'spin' in candidato:
            print('\n')
            temp = candidato.split()
            if len(temp) > 1:
              spin(int(temp[1]))
            else:
              spin()
        elif candidato == 'first':
          first()
        else:
          addCandidato(candidato.capitalize())

    except Exception as e:
      if e:
        print(e)
      print('\nComando não reconhecido, digite uns dos comando expecificados!')
      sleep(3); clear(); entradaDado()

  def main() -> NoReturn :
    try:
      if apresentacao():
        entradaDado()
    except Exception as e:
      print(e)

main()





from typing import Any


class Noh:

  def __init__(self, valor_inicial = None):
    self._dados = valor_inicial
    self._proximo = None
    self.head = None

  def getData(self) -> Any:
    return self._dados

  def getNext(self) -> (Any | None):
    return self._proximo

  def setData(self, novo_valor) -> None:
    if (self._dados[0] == None):
      self._dados.pop()
    self._dados = novo_valor

  def setNext(self, novo_proximo) -> None:
    if (self._proximo[0] == None):
      self._proximo.pop()
    self._proximo = novo_proximo





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
      raise FilaVazia('A Fila está vazia')
    return self._dados.head.getData()

  def dequeue(self):
    if self.isEmpty():
      raise FilaVazia('A Fila está vazia')
    
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
      lista = []
      temp = self._dados
      while (True):
        lista.append(temp.getData())
        if (temp.getNext() == None):
          break
        temp = self.dados.getNext()
      
      return lista
