from fila import *
from os import system, name, _exit
from time import sleep


if __name__ == '__main__':

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
    candidatos.enqueue(novoCandidato)
    print('\nCandidato cadastrado!')
    sleep(3)

  def findAll():
    print(candidatos.mostrar())
    sleep(3)
  
  def spin(numGiros = 1):
    candidatos.girarFila(numGiros)
    sleep(3)
    
  def first():
    print(candidatos.first())
    sleep(3)
    
  def remove():
    candidatos.dequeue()
    sleep(3)

  def entradaDado():
    try:
      while True:
        print('\nGerência de Candidatos Aprovados em Concurso Público.')
        candidato = input('\nInfome o nome do candidato: ').lower().strip()
        if candidato == 'exit':
          _exit(0)
        elif candidato == 'search':
          ...
        elif candidato == 'all':
          print('\n')
          findAll()
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

  def main():
    try:
      if apresentacao():
        entradaDado()
    except Exception as e:
      print(e)

candidatos = Fila()
main()