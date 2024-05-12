import os
import random as rnd
os.system('cls')

lista_frutas = ['morango', 'pitaya', 'melancia', 'framboesa', 'abacaxi']
lista_animais = ['cachorro', 'grilo', 'girafa', 'esquilo', 'serpente']
lista_cores = ['vermelho', 'cinza', 'amarelo', 'preto', 'ciano']

def desenhar_hangman():
    
    if chances ==10:
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        print('             ')
        
    if chances ==9:
        print('             ')
        print('            |')
        print('            |')
        print('            |')
        print('            |')
        print('          ---')
    
    if chances ==8:
        print('      ______')
        print('      |     |')
        print('            |')
        print('            |')
        print('            |')
        print('          ---')
        
    if chances ==7:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('            |')
        print('            |')
        print('          ---')
    
    if chances ==6:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('      |     |')
        print('            |')
        print('          ---')
        
    if chances ==5:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('     /|     |')
        print('            |')
        print('          ---')

    if chances ==4:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('     /|\    |')
        print('            |')
        print('          ---')
        
    if chances ==3:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('     /|\    |')
        print('     /      |')
        print('          ---')
    if chances ==2:
        print('      ______')
        print('      |     |')
        print('    (   )   |')
        print('     /|\    |')
        print('     / \    |')
        print('          ---')
        
    if chances ==1:
        print('      ______')
        print('      |     |')
        print('    (; ;)   |')
        print('     /|\    |')
        print('     / \    |')
        print('          ---')

while True:

    lista = [lista_frutas, lista_animais, lista_cores]

    lista_sorteada = rnd.choice(lista)

    palavra = rnd.choice(lista_sorteada)
    
    chances = 10

    letras_usuario = []
    
    ganhou = False

    while True:
        os.system('cls')
        
        if lista_sorteada == lista_frutas:
            print('FRUTAS')

        elif lista_sorteada == lista_animais:
            print('ANIMAIS')

        elif lista_sorteada == lista_cores:
            print('CORES')
        
        desenhar_hangman()
        
        for letra in palavra:
            
            if letra.lower() in letras_usuario:

                print(letra, end=" ")

            else:

                print("_", end=" ")
        
        print(f"\nVocê tem {chances} chances")
        
        print('HISTÓRICO DE LETRAS:', letras_usuario)    
        
        tentativa = input("Escolha uma letra: ")

        letras_usuario.append(tentativa.lower())

        if tentativa.lower() not in palavra.lower():

            chances -= 1

        ganhou = True

        for letra in palavra:

            if letra.lower() not in letras_usuario:

                ganhou = False

        if chances == 0 or ganhou:
            os.system('cls')
            break
    

    if ganhou:
            print(f"Parabéns, você ganhou! A palavra era {palavra}")

    else:
        if chances ==0:       
            print('      ______')
            print('      |     |')
            print('    (;-;)   |')
            print('     /|\    |')
            print('     / \    |')
            print('          ---')
        print(f"Você perdeu! A palavra era {palavra}")
            
    play = input('Insira ''p'' para continuar jogando ou ''s'' para encerrar o jogo: ')
        
    if play == 's':
            print('Jogo finalizado!')
            break
