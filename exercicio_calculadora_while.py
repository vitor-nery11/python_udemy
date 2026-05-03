# CALCULADORA COM WHILE

while True:
    numero_1 = (input('Digite um numero:'))
    numero_2 = (input('Digite outro numero:'))
    operador = input('Digite o operador (+,-,/,*):')

    numeros_validos = none

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)

    except:
      sair = input('Quer sair ? [s]im:').lower().startswith('s')
      print(sair)

