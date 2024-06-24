import cv2


class Camera:

    def __init__(self) -> None:
        self.video_capture = cv2.VideoCapture(0)

    def open(self):

        ret, frame = self.video_capture.read()
        if not ret:
            return
        else:
            return frame

    def drawingBB(self, frame, top, right, left, bottom, name="Unkown"):

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 0.5, (255, 255, 255), 1)

    def face_crop(self, frame, top, right, left, bottom):

        return frame[top:bottom, left:right]
