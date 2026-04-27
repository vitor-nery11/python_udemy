nome = input('Digite o seu nome:')
peso = float(input('digite o seu peso:'))
altura = float(input('Digite a sua altura:'))

imc = peso/altura **2

print(f'\nO paciente {nome} tem {altura} de altura')
print(f'o seu peso atual é de {peso}')
print(f'O seu imc é de: {imc}')


if imc >= 40:
  print('você esta com obesidade grau III')
elif imc >= 35 and imc <= 39:
  print("você esta com obesidade grau II")
elif imc >= 30 and imc <= 34.9:
  print('você esta com obesidade grau I')
elif imc >= 25 and imc <= 29.9:
  print('você esta com sobrepeso')
elif imc >= 18.6 and imc <= 24.9:
  print('seu peso esta normal')
elif imc <= 18.5:
  print('você abaixo do normal')
else: 
  ('você esta fora dos padrões, busque um atendimento medico')