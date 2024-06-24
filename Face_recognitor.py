import sys
import time
from deepface import DeepFace
from src.camera import Camera
import cv2
import os
from test4 import save_image

cam = Camera()


def facial_recognition(db, frame_thershold=5, time_threshold=5, enable_frame_view=False):
    """
    Recognize the person in the frame
    Args:
        db(str): Database path
        frame_thershold(int): How long should the frame move before freeze
        time_threshold(int): How long should the frame freeze
        enable_frame_view(bool): Should there be a frame gui
    """
    num_frames_with_faces = 0
    freeze = False

    try:
        while True:

            if freeze is False:
                frame = cam.open()

                # clean frame
                raw_frame = frame.copy()

                faces_coordinates = grab_facial_areas(frame)

                if len(faces_coordinates) != 0:
                    frame = highlight_facial_areas(
                        frame, faces_coordinates)

                num_frames_with_faces = num_frames_with_faces + \
                    1 if len(faces_coordinates) else 0

                # move frame for n time(frame thershold)
                freeze = num_frames_with_faces > 0 and num_frames_with_faces % frame_thershold == 0

                if freeze:
                    tic = time.time()

                    for face_location in faces_coordinates:

                        x, y, w, h = face_location

                        cropped_image = raw_frame[y:y+h, x:x+w]
                        dfs = DeepFace.find(
                            img_path=cropped_image,
                            db_path=db,
                            enforce_detection=False
                        )
                        df = dfs[0]

                        # default name
                        name = "unknown"

                        if len(df) > 0:
                            target_path = df["identity"][0]
                            name = target_path.split("\\")[-2]

                            # TODO Go to TTS Function
                            print(f"Familiar Face: {name}")
                        else:
                            save_image(cropped_image)
                            print(f"unfamiliar Face: {name}")

                        frame = highlight_facial_areas(
                            raw_frame, ([face_location]), name)

                    print("Frame Freeze")

            # Freze for n second (time thershold)
            elif freeze is True and time.time() - tic > time_threshold:
                freeze = False
                print("Frame Released")

            if enable_frame_view:
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)

    finally:
        cam.video_capture.release()
        cv2.destroyAllWindows()


def grab_facial_areas(img, detector_backend="opencv", threshold=130):
    """
    Find facial area coordinates in the given image
    Args:
        img (np.ndarray): image itself
        detector_backend (string): face detector backend. Options: 'opencv', 'retinaface',
            'mtcnn', 'ssd', 'dlib', 'mediapipe', 'yolov8', 'centerface' or 'skip'
            (default is opencv).
        threshold (int): threshold for facial area, discard smaller ones
    Returns
        result (list): list of tuple with x, y, w and h coordinates
    """
    try:
        face_objs = DeepFace.extract_faces(
            img_path=img,
            detector_backend=detector_backend,
            # you may consider to extract with larger expanding value
            expand_percentage=0,
            enforce_detection=True
        )
        faces = [
            (
                face_obj["facial_area"]["x"],
                face_obj["facial_area"]["y"],
                face_obj["facial_area"]["w"],
                face_obj["facial_area"]["h"],
            )
            for face_obj in face_objs
            if face_obj["facial_area"]["w"] > threshold
        ]
        return faces
    except:  # to avoid exception if no face detected
        return []


def highlight_facial_areas(img, faces_coordinates, name=""):
    """
    Highlight detected faces with rectangles in the given image
    Args:
        img (np.ndarray): image itself
        faces_coordinates (list): list of face coordinates as tuple with x, y, w and h
        name (str): name to put at the box
    Returns:
        img (np.ndarray): image with highlighted facial areas
    """
    for x, y, w, h in faces_coordinates:
        # highlight facial area with rectangle
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
        cv2.putText(img, name, (x + 6, y - 6),
                    cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
    return img


if __name__ == "__main__":
    facial_recognition("database", enable_frame_view=True)
