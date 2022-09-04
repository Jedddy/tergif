import os
from utils.utils import clear_folder, player
import glob

try:
    os.mkdir('frames')
except FileExistsError:
    pass
        
print("""
 _______ _________ _______    _______  _        _______           _______  _______ 
(  ____ \\__   __/(  ____ \  (  ____ )( \      (  ___  )|\     /|(  ____ \(  ____ )
| (    \/   ) (   | (    \/  | (    )|| (      | (   ) |( \   / )| (    \/| (    )|
| |         | |   | (__      | (____)|| |      | (___) | \ (_) / | (__    | (____)|
| | ____    | |   |  __)     |  _____)| |      |  ___  |  \   /  |  __)   |     __)
| | \_  )   | |   | (        | (      | |      | (   ) |   ) (   | (      | (\ (   
| (___) |___) (___| )        | )      | (____/\| )   ( |   | |   | (____/\| ) \ \__
(_______)\_______/|/         |/       (_______/|/     \|   \_/   (_______/|/   \__/
Made by: Jedddy
Github: https://github.com/Jedddy

# Small sized gifs may cause some issues.
# Very large sized gifs may also cause some issues.
""")

clear_folder() # Clears the frames folder to clean up space.
print('-' * 50)

gif_list = glob.glob('gifs/*.gif')

for num, gifs in enumerate(gif_list):
    print(f'[{num}] {gifs[5:]}')

print('-' * 50)

choice = int(input('Pick a number: '))
gif_choice = os.listdir('gifs')[choice]
player(gif_choice)