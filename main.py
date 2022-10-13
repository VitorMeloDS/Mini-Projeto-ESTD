from fila import *
from os import system, name, _exit
from time import sleep

if __name__ == '__main__':

  clear = lambda: system('cls' if name == 'nt' else 'clear')
  clear()

  def apresentacao() -> bool:
    inicializador = input('\nPara iniciar o processo digite "start", para buscar por algum candidato digite "search", para ver o primeiro candidato digite "first",\npara remover o primeiro candidato digite "remove",  para ver todos os candidatos digite "find all", para girar a fila digite "spin"\ne para sair digite "exit": ').lower().strip()
    print('\nGerência de Candidatos Aprovados em Concurso Público.')
    if inicializador == 'start':
      return True
    elif inicializador == 'search':
      print('\nNão há candidatos para procurar!'); sleep(2); clear(); apresentacao()
      return True
    elif inicializador == 'find all':
      print('\nNão há candidatos para mostrar!'); sleep(2); clear(); apresentacao()
      return True
    elif inicializador == 'remove first':
      print('\nNão há candidatos para remover!'); sleep(2); clear(); apresentacao()
      return True
    elif inicializador == 'spin':
      print('\nNão há candidatos para girar!'); sleep(2); clear(); apresentacao()
      return True
    elif inicializador == 'first':
        print('\nNão há candidatos para mostrar!'); sleep(2); clear(); apresentacao()
        return True
    elif inicializador == 'exit':
      return False
    else:
      print('\nComando não reconhecido, digite uns dos comando expecificados!'); sleep(2); clear(); apresentacao()
      return True

  def addCandidato(novoCandidato):
    candidatos.enqueue(novoCandidato)
    print('\nCandidato cadastrado!')
    sleep(2)

  def findAll():
    print(f'\n{candidatos.mostrar()}')
    sleep(2)
  
  def spin(numGiros = 1):
    candidatos.girarFila(numGiros)
    print(candidatos.mostrar())
    sleep(2)
    
  def first():
    print(candidatos.first())
    sleep(2)
    
  def remove():
    candidatos.dequeue()
    sleep(2)
  
  def search():
    lista = []
    temp = candidatos._dados
    while (True):
      lista.append(temp.getData().lower())
      if (temp.getNext() == None):
        break
      temp = temp.getNext()
    
    return lista

  def validaSearch():
    nome = input('\nDigite o nome que deseja procurar: ').lower().strip()
    lista_temp_2 = nome.split()
    if len(lista_temp_2) > 1:
      str_temp_2 = ''
      for j in lista_temp_2:
        str_temp_2 += f'{j.capitalize()} '
      if nome in search():
        print(f'\n{str_temp_2}existe na lista!')
      else:
        print(f'\n{str_temp_2}não existe na lista!')
    else:
      if nome in search():
        print(f'\n{nome.capitalize()} existe na lista!')
      else:
        print(f'\n{nome.capitalize()} não existe na lista!')  

  def entradaDado():
    try:
      while True:
        candidato = input('\nInfome o nome do candidato: ').lower().strip()
        if candidato == 'exit':
          _exit(0)
        elif candidato == 'search':
          if candidatos.isEmpty():
            print('\nNão há candidatos para procurar')
          else:
            validaSearch()
        elif candidato == 'all':
          findAll()
        elif candidato == 'remove':
          remove()
          if not candidatos.isEmpty():
            print('\nCandidato removido\n')
          findAll()
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
          lista_temp = candidato.split()
          if len(lista_temp) > 1:
            str_temp = ''
            for i in lista_temp:
              str_temp += f'{i.capitalize()} '
            candidato = str_temp.strip()
            addCandidato(candidato)
          else:
            addCandidato(candidato.capitalize())

    except Exception as e:
      if e:
        print(e)
      print('\nComando não reconhecido, digite uns dos comando expecificados!')
      sleep(2); clear(); entradaDado()

  def main():
    try:
      if apresentacao():
        entradaDado()
    except Exception as e:
      print(e)

candidatos = Fila()
main()  
