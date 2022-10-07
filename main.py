from typing import NoReturn
from noh import *
from os import system, name, _exit
from time import sleep


if __name__ == '__main__':
  candidatos = Noh(None)

  clear = lambda: system('cls' if name == 'nt' else 'clear')
  clear()

  def apresentacao() -> bool:
    inicializador = input('\nPara iniciar o processo digite "start", para buscar por algum candidato digite "search", para remover o primeiro candidato digite "remove first", para ver todos os candidatos digite "find all", para girar a fila digite "girar" e para sair digite "exit": ').lower().strip()

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
    elif inicializador == 'exit':
      return False
    else:
      print('\nComando não reconhecido, digite uns dos comando expecificados!'); sleep(3); clear(); apresentacao()
      return True

  def addCandidato(novoCandidato):
    candidatos.setData(novoCandidato)
    print('Candidato cadastrado!')

  def findAll():
    return candidatos.getData()

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
          print(findAll())
          ...
        elif candidato == 'remove first':
          ...
        else:
          addCandidato(candidato)

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

