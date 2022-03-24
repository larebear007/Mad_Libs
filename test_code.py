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

story_1 = f'''There once was a {adj} {animal} named, {name}. It lived in the country {country}, 
and for all its life it
had always grazed on {foods}.'''

print(type(story_1))
# for letter in story_1:
#     print(story_1, end='')
#     time.sleep(.15)
