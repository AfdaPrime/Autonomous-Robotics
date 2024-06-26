#!/usr/bin/env python3

import cv2
import face_recognition
import rospy
from std_msgs.msg import String
import json
import numpy as np
import sys
from face_recognition_pkg.srv import strangerPrompt

video_capture = cv2.VideoCapture(0) 

current_faces=[]

def main():

    stranger = rospy.ServiceProxy('strangerPrompt',strangerPrompt)

    pub = rospy.Publisher("gtts_text",String,queue_size = 10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        ret, frame = video_capture.read()
        
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame,face_locations)

        with open("/home/vboxuser/ws_catkin/database/data.json","r") as f:
            file_data = json.load(f)
    

        for (top,right,bottom,left), face_encodings in zip(face_locations,face_encodings):

            # if the face is new it will check if the system knows who is it
            matches = face_recognition.compare_faces(file_data["person_details"]["encode"], face_encodings)

            name = "unknown"

            if True in matches:

                first_match_index = matches.index(True)
                name = file_data["person_details"]["name"][first_match_index]

                if not name in current_faces:
                    msg = String()
                    msg.data = name
                    pub.publish(msg)
            else: # if a stranger it will prompt voice recognition
                respl = stranger()
                res = respl.respond

                if res != "stranger": #if the user wanted to save the name thus the name is save
                    name = res
                    write_json(np.ndarray.tolist(face_encodings),name)
                # else:
                '''
                    enter stanger database
                    have the above checking to check the stranger database also so that no repeat question
                    find a way to detect if the stranger face is no longer in the frame from 30 delete the stranger data
                    find a way also to have the know person the send on one msg to tts
                        maybe have a current face database and the progeam must chage this database first
                        then after 1 min not detect delete the current face database
                '''

            current_faces.append(name)

            cv2.rectangle(frame,(left,top),(right,bottom), (0,0,255),2)
            cv2.putText(frame,name, (left,top-10),cv2.FONT_HERSHEY_SIMPLEX, 0.9,(0,0,255),2)

        cv2.imshow("Video",frame)

        if cv2.waitKey(1) & 0xFF == ('q'):
            break

        rate.sleep()

    video_capture.release()
    cv2.destroyAllWindows
    sys.exit(0)

def write_json(new_data,name,filename="/home/vboxuser/ws_catkin/database/data.json"):

    with open(filename,'r+') as file:

        file_data = json.load(file)

        file_data["person_details"]["encode"].append(new_data)
        file_data["person_details"]["name"].append(name)

        file.seek(0)

        json.dump(file_data,file,indent=4)

if __name__ == '__main__':
    rospy.init_node('face_node', anonymous=True)
    rospy.wait_for_service('strangerPrompt')
    main()