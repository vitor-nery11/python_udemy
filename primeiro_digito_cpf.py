# verificando primeiro digito do cpf

lista_multiplicação = []

cpf = '03588082514'
digitos = cpf[:9]
contador_regressivo = 10

resultado = 0 
for digito in digitos:
     resultado += int(digito) * contador_regressivo
     contador_regressivo -= 1
digito = (resultado * 10 ) % 11

# logica para decidir o primeiro digito

digito = digito if digito <= 9 else 0 
print(digito)

