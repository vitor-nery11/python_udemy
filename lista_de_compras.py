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
      lista_compras.append(input('digite o que deseja adicionar:'))
  elif escolha == 2:
      for indice,item in enumerate(lista_compras):
          print(indice, item)
      lista_compras.pop(int(input('digite o numero do que deseja remover:')))
      print(lista_compras)
  elif escolha == 3:
      for indice,item in enumerate(lista_compras):
          print('\n')
          print(indice, item)
  elif escolha == 4:
      print('obrigado por usar a nossa lista!!')
      break
  else:
      print('Houve algum erro, reinicie o sistema')
      



