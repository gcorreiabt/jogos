import random
import time

erro = 0
acerto = 0

print("""____________________
|    Seja bem vindo ao    |
| **** QUIZ ANIMAL **** |
|vvvvvvvvvvvvvvvvvvvvv|
¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ \n""" )     #Intro

print("""Regras: Leia atentamente a questão e responda a letra que você acredita ser a resposta correta.
Ex: \"Quantas asas tem uma galinha?\". Resposta: A \n \n""")                #Explicação



perguntas = ["Quantas corcovas possui um camelo?", "Qual animal tem uma dieta exclusiva de eucaliptos?",
             "Qual o único mamífero que consegue voar?", "Quantos corações o polvo tem?",
             "Qual animal é Conhecido por levantar até 50 vezes o próprio peso?", "Qual animal é comumento conhecido pelas suas \'risadas\'?",
             "Qual mamífero coloca ovos?", "Qual desses animais não é um mamífero?",
             "Qual animal utiliza Ecolocalização?", "Qual desses animais não é um peixe?",
             "A qual espécie pertence o Homem moderno?", "Qual desses não pertence a ordem dos cetáceos?",
             "Qual destes não é um inseto?", "Qual é o maior felino do mundo?",
             "Qual dos seguintes insetos não é um aracnídeo?"]

respostas = ["\n A) 5 \n B) 1 \n C) 2 \n D) 3,5" , "\n A) Bicho-preguiça \n B) Baleia \n C) Girafa \n D) Coala",
             "\n A) Morcego \n B) Galinha \n C) Pinguim \n D) Coruja", "\n A) 7 \n B) 2 \n C) 5 \n D) 3",
             "\n A) Formiga \n B) Rinoceronte \n C) Gorila \n D) Baleia", "\n A) Humano \n B) Chimpanzé \n C) Hiena \n D) Raposa",
             "\n A) Pinguim \n B) Baleia \n C) Ornitorrinco \n D) Coala", "\n A) Baleia \n B) Tubarão \n C) Golfinho \n D) Orca",
             "\n A) Morcego \n B) Formiga \n C) Topeira \n D) Minhoca", "\n A) Tubarão \n B) Baleia \n C) Arraia \n D) Enguia",
             "\n A) Homo erectus \n B) Neandertais \n C) Homo sapiens \n D) Homossexuais", "\n A) Baleia \n B) Leão marinho \n C) Orca \n D) Golfinho",
             "\n A) Aranha \n B) Formiga \n C) Besouro \n D) Vagalume", "\n A) Onça pintada \n B) Leopardo \n C) Leão \n D) Tigre",
             "\n A) Escorpião \n B) Opilião \n C) Ácaro \n D) Carrapato"]

                                                                                                                                                                                                                          #configuração questões
correta = ["C", "D", "A", "D", "A", "C", "C", "B", "A", "B", "C", "B", "A", "D", "B"]




while acerto+erro != 10:

  questoes = random.randint(0, len(perguntas) - 1)


  print(f"|{perguntas[questoes]}| \n {respostas[questoes]} \n")

  chute = str(input("Qual a resposta correta?: \n \n")).upper()   #upper para transformar as letras em maiúscula

  while chute != "A" and chute != "B" and chute != "C" and chute != "D":
    print("Resposta inválida! Escolha uma das 4 letras disponíveis...  \n \n")

    time.sleep(1.5)

    print(f"|{perguntas[questoes]}| \n {respostas[questoes]} \n")
    chute = str(input("Qual a resposta correta?: \n \n")).upper()                                                               #ARRUMAR
    

  if chute != correta[questoes]:
    print("****Errado! A resposta correta era {}**** \n \n".format(correta[questoes]))

    erro += 1

    perguntas.pop(questoes)
    respostas.pop(questoes)         #tirar a pergunta para não repetir
    correta.pop(questoes)

    time.sleep(2)

  else:
    print("Acertou! \n \n")

    acerto += 1

    perguntas.pop(questoes)
    respostas.pop(questoes)         #tirar a pergunta para não repitir
    correta.pop(questoes)

    time.sleep(2)


if erro > 3:
  print("Acabou o jogo!! Você acertou um total de {} e errou {} questões. Melhore...".format(acerto, erro))
                                                                                                              #Resultado
else:
  print("Acabou o jogo!! Você acertou um total de {} e errou {} questões. Parabéns!!!".format(acerto, erro))

time.sleep(3)