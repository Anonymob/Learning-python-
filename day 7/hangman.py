import random
word_list = ["camel","elephant","lion","tiger","cheeta","lepord","kangaroo","wolf","bear","hippopotamous"]
ascii_art = [
 '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''   
,'''
  +---+
  |   |
  O   |
      |
      |
      |
=========

''',
'''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
 +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
,
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]
art = ascii_art[::-1]


lives = 6
word = random.choice(word_list)

hidden_word = ""

for i in range(len(word)):
    hidden_word += "_"

print(hidden_word)

flag = False

end_guess = []


while not flag:
    output = ""
    usr_input = input("Guess a letter - ")
    for i in word:
        
        if i==usr_input:
            output+=i
            end_guess.append(i)
            
        elif i in end_guess:
            output+=i
        else:
            output+="_"
        
    if usr_input not in word:
        lives-=1
        print(art[lives])
        print(f"your guess was wrong! you just lost a life - {lives} left")
        if lives ==0:
            print("you lose")
            flag = True

    if "_" not in output:
        flag = True
    print(output)
    
        
