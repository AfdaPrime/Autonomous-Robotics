import camera
import cv2
import detectPerson

if __name__ == "__main__":

    cam = camera.Camera()
    det = detectPerson.DetectPerson()
    while True:

        frame = cam.open()

        det.face_recognition(frame)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.video_capture.release()
    cv2.destroyAllWindows()
