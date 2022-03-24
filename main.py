# MAD LIBS

# SPECIFICATIONS: Create a program that contains a script with some lines left blank for user input.
# Prompt the user for input to fill in the blanks, asking for appropriate parts of speech.
# After the user has entered in their contents, print out the story script with their entries to reveal
# their unique (and probably hilarious) story. Advanced Features: 1. A loop that allows them to play the
# game continuously, 2. A menu bar with 2-3 story templates to choose from, 3. color-coded words to
# differentiate the user-input words from the story script.


def story1():
    import time

    blue = "\033[0;34m"
    end = "\033[0m"

    print('\nLet\'s get started!')
    time.sleep(1)
    print('Please add some of your own words to make this story uniquely your own ...\n')
    time.sleep(1)

    adj = blue + input('Adjective: ') + end
    animal = blue + input('Animal: ') + end
    country = blue + input('Country: ') + end
    name = blue + input('Name: ') + end
    foods = blue + input('Foods (plural): ') + end

    story_1 = f'''\nThere once was a {adj} {animal} named, {name}. It lived in the country {country}, 
and for all its life it had always grazed on {foods}.'''
    print('Generating story ...')
    time.sleep(3)
    for letter in story_1:
        print(letter, end='')
        time.sleep(.09)


def story2():
    blue = "\033[0;34m"
    end = "\033[0m"

    print('\nLet\'s get started!')
    time.sleep(1)
    print('Please add some of your own words to make this story uniquely your own ...\n')
    time.sleep(1)

    adj = blue + input('Adjective: ') + end
    animal = blue + input('Animal: ') + end
    country = blue + input('Country: ') + end
    name = blue + input('Name: ') + end
    foods = blue + input('Foods (plural): ') + end

    story_2 = f'''There once was a {adj} {animal} named, {name}. It lived in the country {country}, 
and for all its life it had always grazed on {foods}.'''
    print('Generating story ...')
    time.sleep(3)
    for letter in story_2:
        print(letter, end='')
        time.sleep(.09)


def story3():
    blue = "\033[0;34m"
    end = "\033[0m"

    print('\nLet\'s get started!')
    time.sleep(1)
    print('Please add some of your own words to make this story uniquely your own ...\n')
    time.sleep(1)

    adj = blue + input('Adjective: ') + end
    animal = blue + input('Animal: ') + end
    country = blue + input('Country: ') + end
    name = blue + input('Name: ') + end
    foods = blue + input('Foods (plural): ') + end

    story_3 = f'''There once was a {adj} {animal} named, {name}. It lived in the country {country}, 
and for all its life it had always grazed on {foods}.'''
    print('Generating story ...')
    time.sleep(3)
    for letter in story_1:
        print(letter, end='')
        time.sleep(.09)


import time

while True:
    print('Hello! Welcome to Mad Libs!')
    time.sleep(1)
    print('To get started, please choose your story ...\n')
    time.sleep(1)
    print('OPTION 1: The Unexpected Fruit of No Labor')
    time.sleep(1)
    print('OPTION 2: Something')
    time.sleep(1)
    print('OPTION 3: something')
    time.sleep(1)
    while True:
            story = input('Please enter 1, 2, or 3 for your story choice: ')
            if story == '1':
                story1()
                break
            if story == '2':
                story2()
                break
            if story == '3':
                story3()
                break
            else:
                print('Please enter the number 1, 2, or 3 as your story option. No funny business!')
                continue

    restart = input('\n\nThanks for playing Mad Libs! Would you like to play again? ')
    if restart.lower() == 'yes' or restart.lower() == 'y':
        print('\n')
        continue
    else:
        print('\nCome back any time!')
        break
quit()
