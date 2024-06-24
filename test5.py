import os

diretory_list = os.listdir("stranger_image")

print(diretory_list)

os.mkdir(f"database/Freein")
os.replace(
    f"stranger_image/1a.png", f"database/Freein/Freein1.png")
