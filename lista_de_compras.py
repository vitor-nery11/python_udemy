"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

# minha resolução 


import os

print('\n')
print('bem vindo a sua lista de compras')

lista_compras = []

while True:
  print('o que deseja fazer?')
  print('1. adicionar produto')
  print('2. apagar produtos')
  print('3. listar produtos')
  print('4. sair')
  print('\n')

  escolha = int(input('Digite a sua escolha:'))

  if escolha == 1:
      os.system('clear')
      lista_compras.append(input('digite o que deseja adicionar:'))

  elif escolha == 2:
      for indice,item in enumerate(lista_compras, start=1):
          print(indice, item)
      lista_compras.pop(int(input('digite o numero do que deseja remover:')))
      print(lista_compras)
  
  elif escolha == 3:
      os.system('clear')
      for indice,item in enumerate(lista_compras, start=1): 
          print(indice, item)
      print('\n')

  elif escolha == 4:
      print('obrigado por usar a nossa lista!!')
      break
  else:
      print('Houve algum erro, reinicie o sistema')
      



