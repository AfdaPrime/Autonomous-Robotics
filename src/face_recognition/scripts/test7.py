#!/usr/bin/env python3

import cv2
import face_recognition
import rospy
from std_msgs.msg import String

known_face_encodings = []
known_face_names = []

known_person1_image = face_recognition.load_image_file("/home/vboxuser/ws_catkin/database/Ajiz/Ajiz1.png")
known_person2_image = face_recognition.load_image_file("/home/vboxuser/ws_catkin/database/Master/Master1.png")

know_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
know_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]

known_face_encodings.append(know_person1_encoding)
known_face_encodings.append(know_person2_encoding)

known_face_names.append("Ajiz")
known_face_names.append("Master")

video_capture = cv2.VideoCapture(0) 

def main():

    pub = rospy.Publisher("gtts_text",String,queue_size = 10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():

        ret, frame = video_capture.read()

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame,face_locations)

        for (top,right,bottom,left), face_encodings in zip(face_locations,face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encodings)

            name = "Unkown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                msg = String()
                msg.data = name
                pub.publish(msg)

            cv2.rectangle(frame,(left,top),(right,bottom), (0,0,255),2)
            cv2.putText(frame,name, (left,top-10),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(0,0,255),2)

        cv2.imshow("Video",frame)

        if cv2.waitKey(1) & 0xFF == ('q'):
            break

        rate.sleep()

    video_capture.release()
    cv2.destroyAllWindows

if __name__ == '__main__':
    rospy.init_node('face_node', anonymous=True)
    main()