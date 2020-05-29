# Write your code here
import random
import string


print('H A N G M A N')
menu_choice = ''
while menu_choice != 'exit':
    print('Type "play" to play the game, "exit" to quit:')
    input_choice = input()

    if input_choice == 'play':
        print()
        language = ['python', 'java', 'kotlin', 'javascript']
        random_lang = random.choice(language)
        underscores = len(random_lang) * '-'
        used_words = []
        list_underscores = []
        list_underscores.extend(underscores)
        print(underscores)

        lives = 8
        while lives > 0:
            print("Input a letter")
            letter = input()
            if len(letter) < 1 or len(letter) > 1:
                print("You should input a single letter")
                print()
                print("".join(list_underscores))
                continue
            if letter not in string.ascii_lowercase:
                print("It is not an ASCII lowercase letter")
                print()
                print("".join(list_underscores))
                continue
            if letter in used_words:
                print("You already typed this letter")
                print()
                print("".join(list_underscores))
                continue
            used_words.append(letter)
            if letter in random_lang:
                indexes = [i for i, a in enumerate(random_lang) if a == letter]
                for i in indexes:
                    list_underscores[i] = letter
                if "".join(list_underscores) == random_lang:
                    print("You survived!")
                    break
            else:
                print("No such letter in the word")
                lives -= 1
                if lives == 0:
                    print("You are hanged!")
            print()
            print("".join(list_underscores))
    elif input_choice == 'exit':
        menu_choice = 'exit'



