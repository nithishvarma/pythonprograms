import os
import random
import sys
word=[
    'apple',
    'bannana',
    'lime',
    ]
def welcome():
    ch=input('press s to proceed n to exist').lower()
    if ch=='n':
        print('bye')
        sys.exit()
def draw(bad_guess,good_guess,secret_word):
    print('Strikes: {}/7'.format(len(bad_guess)))
    print('')

    for letter in bad_guess:
        print(letter,end='')
    print(' ')
    for letter in secret_word:
          if letter in good_guess:
                print(letter,end='')
          else:
               print('_',end='')
    print(' ')
          
def getguess(bad_guess,good_guess):
          g=input('enter letter buddy')
          if g in good_guess or bad_guess:
                print('you typed the letter')
          else:
              return g
          
def play(done):
    secret_word=random.choice(word)
    bad_guess=[]
    good_guess=[]
    complete=True       
    while True:
        draw(bad_guess,good_guess,secret_word)
        guess=getguess(bad_guess,good_guess)
        if guess in secret_word:
               good_guess.append(guess)
               complete=True
               for i in range(len(secret_word)):
                     if secret_word[i] not in good_guess:
                            complete=False
               if complete:
                    print('you won')
                    print('yout word is',good_guess)
                    done=True
        else:
                bad_guess.append(guess)
                if(len(bad_guess)==7):
                    print('you lost buddy')
                    done=True
        if done:
              ch=input('press n to exist and y to play again')
              if ch=='n':
                    sys.exist()
              else:
                    return play(done=False)
          
                  
          
                   
print('welcome to letter game')
welcome()
play(done=False)
