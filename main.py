# MAD LIBS

# SPECIFICATIONS: Create a program that contains a script with some lines left blank for user input.
# Prompt the user for input to fill in the blanks, asking for appropriate parts of speech.
# After the user has entered in their contents, print out the story script with their entries to reveal
# their unique (and probably hilarious) story. Advanced Features: 1. A loop that allows them to play the
# game continuously, 2. A menu bar with 2-3 story templates to choose from, 3. color-coded words to
# differentiate the user-input words from the story script.




def story1():
    blue = "\033[0;34m"
    end = "\033[0m"

    adj = blue + input('Adjective: ') + end
    animal = blue + input('Animal: ') + end
    country = blue + input('Country: ') + end
    name = blue + input('Name: ') + end
    foods = blue + input('Foods (plural): ') + end

    story1 = f'''There once was a {adj} {animal} named, {name}. It lived in the country {country}, and for all its life it
    had always grazed on {foods}.'''
    print(story1)


story1()
