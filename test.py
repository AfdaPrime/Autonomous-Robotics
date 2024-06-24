from deepface import DeepFace
from src.camera import Camera
import json
import cv2
cam = Camera()

# dfs = DeepFace.find(
#     img_path="database\Master\Master1.png",
#     db_path="database",
# )
# df = dfs[0]

# candidate = df.iloc[0]
# target_path = candidate["identity"]
# target_img = cv2.imread(target_path)

# print(target_path.split("\\")[-2])


frame = cam.open()
face_objs = DeepFace.extract_faces(
    img_path=frame,
    detector_backend="opencv",
    # you may consider to extract with larger expanding value
    expand_percentage=0,
    enforce_detection=False
)
faces = [
    (
        face_obj["facial_area"]["x"],
        face_obj["facial_area"]["y"],
        face_obj["facial_area"]["w"],
        face_obj["facial_area"]["h"],
    )
    for face_obj in face_objs

]
for i, face_location in enumerate(faces):
    frame_cropped = frame.copy()
    x, y, w, h = face_location
    print(frame.shape)
    print(x, y, w, h)
    frame_cropped = frame_cropped[y:y+h,x:x+w]
    print(frame.shape)

    cv2.imshow(f'person {i}', frame_cropped)
    cv2.waitKey(0)
# if cv2.waitKey(1) & 0xFF == ord('q'):
#     break

cam.video_capture.release()
cv2.destroyAllWindows()
# print(faces)


# def stream(
#     db_path: str = "",
#     model_name: str = "VGG-Face",
#     detector_backend: str = "opencv",
#     distance_metric: str = "cosine",
#     enable_face_analysis: bool = True,
#     source: Any = 0,
#     time_threshold: int = 5,
#     frame_threshold: int = 5,
# ) -> None:
#     """
#     Run real time face recognition and facial attribute analysis

#     Args:
#         db_path (string): Path to the folder containing image files. All detected faces
#             in the database will be considered in the decision-making process.

#         model_name (str): Model for face recognition. Options: VGG-Face, Facenet, Facenet512,
#             OpenFace, DeepFace, DeepID, Dlib, ArcFace, SFace and GhostFaceNet (default is VGG-Face).

#         detector_backend (string): face detector backend. Options: 'opencv', 'retinaface',
#             'mtcnn', 'ssd', 'dlib', 'mediapipe', 'yolov8', 'centerface' or 'skip'
#             (default is opencv).

#         distance_metric (string): Metric for measuring similarity. Options: 'cosine',
#             'euclidean', 'euclidean_l2' (default is cosine).

#         enable_face_analysis (bool): Flag to enable face analysis (default is True).

#         source (Any): The source for the video stream (default is 0, which represents the
#             default camera).

#         time_threshold (int): The time threshold (in seconds) for face recognition (default is 5).

#         frame_threshold (int): The frame threshold for face recognition (default is 5).
#     Returns:
#         None
#     """

#     time_threshold = max(time_threshold, 1)
#     frame_threshold = max(frame_threshold, 1)

#     streaming.analysis(
#         db_path=db_path,
#         model_name=model_name,
#         detector_backend=detector_backend,
#         distance_metric=distance_metric,
#         enable_face_analysis=enable_face_analysis,
#         source=source,
#         time_threshold=time_threshold,
#         frame_threshold=frame_threshold,
#     )
