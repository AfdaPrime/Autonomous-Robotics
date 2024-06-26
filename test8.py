#!/bin/python3

import face_recognition
import json 
import numpy as np

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

def write_json(new_data,name,filename="data.json"):

    with open(filename,'r+') as file:

        file_data = json.load(file)

        file_data["person_details"]["encode"].append(new_data)
        file_data["person_details"]["name"].append(name)

        file.seek(0)

        json.dump(file_data,file,indent=4)


known_person2_image = face_recognition.load_image_file("/home/vboxuser/ws_catkin/database/Master/Master2.jpg")
know_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]

print(np.size(know_person2_encoding))

# y = {"name":"Sim",
#      "encode":np.ndarray.tolist(know_person2_encoding)}

write_json(np.ndarray.tolist(know_person2_encoding),"Master")

# with open("data.json","r") as f:
#     file_data = json.load(f)

#     print(len(file_data["person_details"]))
#     # print(np.size(np.array(file_data["person_details"][0]["encode"])))
#     matches = face_recognition.compare_faces(file_data["person_details"]["encode"],know_person1_encoding)

#     print(matches)