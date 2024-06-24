import face_recognition as fr
import camera
import json


class FaceEncoder:

    def __init__(self) -> None:
        pass

    def encoder(self, frame, name, top, right, left, bottom):
        face_encoding = fr.face_encodings(
            frame, [[top, right, left, bottom]])[0]

        json_data = {
            "encode": face_encoding.tolist(),
            "voice": "FUTURE UPDATE"}

        with open(file, 'r+') as f:
            # First we load existing data into a dict.
            file_data = json.load(f)
            # Join new_data with file_data inside emp_details
            file_data["stranger"].append(json_data)
            # Sets file's current position at offset.
            f.seek(0)
            # convert back to json.
            json.dump(file_data, f, indent=4)


if __name__ == "__main__":

    # Import packages
    import cv2
    import numpy as np
    import face_recognition as fr

    img = cv2.imread('img\img2.jpg')
    fEnc = FaceEncoder()

    face_locations = fr.face_locations(img)

    for face_location in face_locations:
        top, right, bottom, left = face_location
        fEnc.encoder(img, "db\stranger.json", top, right, left, bottom)
