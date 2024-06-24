import face_recognition as fr
import cv2
from camera import Camera
from faceEncoder import FaceEncoder
from deepface import DeepFace


class DetectPerson:

    def __init__(self) -> None:
        self.cam = Camera()
        self.fEnc = FaceEncoder()

    def face_recognition(self, frame):

        face_locations = fr.face_locations(frame)

        for face_location in face_locations:
            top, right, bottom, left = face_location

            dfs = DeepFace.find(
                img_path=frame,
                db_path="database",
            )
            df = dfs[0]

            candidate = df.iloc[0]
            target_path = candidate["identity"]
            target_img = cv2.imread(target_path)

            # face_encoding = fr.face_encodings(frame, [face_location])[0]
            # matches = fr.compare_faces(
            #     self.known_face_encodings, face_encoding, tolerance=0.6)

            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = self.known_names[first_match_index]
            # else:
            #     # Thread later
            #     self.fEnc.encoder(frame, top, right, left, bottom)
            #     name = "Unkown"

            # self.cam.drawingBB(frame, top, right, left, bottom, name)
