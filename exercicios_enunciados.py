# Primeiro exercicio - Par ou Impar

entrada = input('Digite um numero:')

if entrada == '':
  print('você não digitou nada')
else:
  try:
    numero_int = int(entrada)

    if numero_int % 2 == 0:
      print(f'o numero {numero_int} é par')
    else:
      print(f'o numero {numero_int} é impar')
  except ValueError:
      print('você não digitou um numero inteiro valido')

# Segundo exercicio - Saudação

entrada = int(input('Digite que horas são:'))

try:  
  hora_int = int(entrada )
  if hora_int >= 0 and hora_int <= 11:
    print('Bom dia!!')
  elif hora_int >= 12 and hora_int <= 17:
    print('Boa tarde!!')
  elif hora_int >= 18 and hora_int <= 23:
    print('Boa noite!!')
  else:
    print('Erro, reinicie o sistema.')

except ValueError:
    print('Você não digitou um valor inteiro')




# Terceiro exercicio - Contador nome

#declarando variavel
nome = input('Digite o seu primeiro nome:')

#logica 

if nome > 1:
  if len(nome) <= 4:
    print('Seu nome é curto')
  elif len(nome) >= 5 and len(nome) <= 6:
    print('seu nome é normal')
  elif len(nome) > 6:
    print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra')
