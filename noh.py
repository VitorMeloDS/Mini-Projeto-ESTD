

from typing import Any


class Noh:

  def __init__(self,valor_inicial):
    self._dados = [valor_inicial]
    self._proximo = [None]

  def getData(self) -> Any:
    return self._dados

  def getNext(self) -> (Any | None):
    return self._proximo

  def setData(self, novo_valor) -> None:
    self._dados += [novo_valor]

  def setNext(self, novo_proximo) -> None:
    if (self._proximo[0] == None):
      self._proximo.pop()
    self._proximo += [novo_proximo]




