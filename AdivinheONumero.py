import random

a = 0
tentativa = 0
novamente = 'sim'
jogar = ['sim', 'SIM', 'Sim', 's', 'S']

print('****************************************')
print('Bem vindo ao jogo de Adivinhação!')
print('****************************************')

print()

print('Descubra o valor secreto entre 1 e 500')

while a < 3:
  print()
  a += 1


while novamente in jogar:

  tentativa = 0


  num = random.randint(1, 500)

# num = int(input('Escolha um número de 1 a 500: '))
# while num > 500 or num < 1:
#   print('Escolha um valor válido!!')                          #seção de número manual
#   print()
#   num = int(input('Escolha um número de 1 a 500: '))


  print()
  print('///////////////////////////////////////////////////')
  print()


  chute = int(input('Chute um número: '))



  while chute != num:

    distancia = (num - chute)

    if distancia >= 20 and distancia < 100:
      print('Mais alto.')
      print()
      tentativa = tentativa + 1

    elif distancia >= 100:
      print('Você está muito baixo!')
      print()
      tentativa = tentativa + 1

    elif distancia >= 1 and distancia < 20:
      print('Um pouco mais alto..')
      print()
      tentativa = tentativa + 1

    elif distancia <= -20 and distancia > -100:
      print('Mais baixo.')
      print()
      tentativa = tentativa + 1

    elif distancia <=  -100:
      print('Você está muito alto!')
      print()
      tentativa = tentativa + 1

    elif distancia <= -1 and distancia > -20:
      print('Um pouco mais baixo..')
      print()
      tentativa = tentativa + 1


    print('///////////////////////////////////////////////////')
    print()
    chute = int(input('Chute um número: '))

  tentativa += 1
  print('-------------------------------------------------------------')
  print()
  print('Parabéns, você acertou! A resposta era: ' + str(num))
  print(f'Você acertou em {tentativa} tentativas')
  print()

  novamente = input('Quer jogar novamente? (sim/não): ')