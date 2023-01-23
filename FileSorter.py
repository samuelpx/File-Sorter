import os, shutil, time, keyboard, re
from os import path

#Add more image types or categories at will

image_types = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg', '.jfif', '.mp4'] #
categories = ['cats', 'videogames', 'people', 'places', 'food', 'cars', 'technology', 'other', 'test', 'memes', 'video','gif']
print(f'  ___   ____    ____   ____  ____   ____  _____   ____  ___     ___   ____       ____  __ __ ')
print(f' /   \ |    \  /    | /    ||    \ |    ||     | /    ||   \   /   \ |    \     |    \|  |  |')
print(f'|     ||  D  )|   __||  o  ||  _  | |  | |__/  ||  o  ||    \ |     ||  D  )    |  o  )  |  |')
print(f'|  O  ||    / |  |  ||     ||  |  | |  | |   __||     ||  D  ||  O  ||    /     |   _/|_   _|')
print(f'|     ||    \ |  |_ ||  _  ||  |  | |  | |  /  ||  _  ||     ||     ||    \     |  |  |     |')
print(f'|     ||  .  \|     ||  |  ||  |  | |  | |     ||  |  ||     ||     ||  .  \    |  |  |  |  |')
print(f' \___/ |__|\_||___,_||__|__||__|__||____||_____||__|__||_____| \___/ |__|\_|    |__|  |__|__|\n\n\n')


print(f'Starting sorting program!!')
print('Press "ctrl+alt+q" to quit the program')
print('Press "ctrl+alt+p" to pause scanning the folder')
print('Press "ctrl+alt+s" to re-start scanning the folder')
print('Press "ctrl+alt+c+a" to input more categories')

sortedFolder = ""  # Set folder path here

while True:
    for file in os.listdir(sortedFolder):
        if file.endswith(tuple(image_types)):
            for category in categories:
                if category in file and not path.exists(f'{sortedFolder}/{category}'):
                    os.makedirs(f'{sortedFolder}/{category}')
                    shutil.move(f'{sortedFolder}/{file}', f'{sortedFolder}/{category}')
                elif path.exists(f'{sortedFolder}/{category}/{file}'):
                    os.remove(f'{sortedFolder}/{file}')
                elif category in file and path.exists(f'{sortedFolder}/{category}'):
                    shutil.move(f'{sortedFolder}/{file}', f'{sortedFolder}/{category}')
    if keyboard.is_pressed('ctrl+alt+q'):
        print(f'Quitting!!')
        break
    if keyboard.is_pressed('ctrl+alt+p'):
        print(f'Paused!!')
        while True:
            if keyboard.is_pressed('ctrl+alt+s'):
                print(f'Restarting!')
                break
            if keyboard.is_pressed('ctrl+alt+q'):
                break
    if keyboard.is_pressed('ctrl+alt+c+a'):
        while True:
            print('Input more categories, separate them with a comma')
            input_categories = input()
            if re.match(r'^[a-zA-Z,]+$', input_categories):
                input_categories = input_categories.split(',')
                for category in input_categories:
                    categories.append(category)
                break
            else:
                print('Invalid input')
    time.sleep(1)
