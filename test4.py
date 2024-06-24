import time
import cv2
import numpy as np
from deepface import DeepFace
import threading
import os

DIRECTORY_PATH = "stranger_image"


def save_image(frame):

    sub_thread = threading.Thread(target=user_input)

    dfs = DeepFace.find(
        img_path=frame,
        db_path="stranger_image",
        enforce_detection=False
    )
    df = dfs[0]

    if len(df) <= 0:
        cv2.imwrite(f"stranger_image/{time.time()}.png", frame)

    user_input()

    # if not sub_thread.is_alive():

    #     sub_thread.start()


def user_input():

    # TODO make sure that the face in stranger is no on cam
    diretory_list = os.listdir(DIRECTORY_PATH)

    while len(diretory_list) > 2:

        x = input("Do you want to add this person to your contact")
        if x == "YES":
            x = input("What thier name")
            os.mkdir(f"database/{str.capitalize(x)}")
            os.replace(
                f"stranger_image/{diretory_list[0]}", f"database/{str.capitalize(x)}/{str.capitalize(x)}1.png")
        else:
            os.remove(f"stranger_image/{diretory_list[0]}")
        diretory_list = os.listdir(DIRECTORY_PATH)
