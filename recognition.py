import cmake 
import dlib 
import face_recognition
import cv2 
import os
import numpy as np
from datetime import datetime

def markAttendance(name):
    with open('sheet.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            f.flush()

                
image_list = []
image_encodings = []
path = os.listdir('students')
print(path)
rel = "students/" 
for i in range(len(path)):
    image_list.append(face_recognition.load_image_file(rel+ path[i]))
    try:
        image_encodings.append(face_recognition.face_encodings(image_list[i])[0])
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

#Names
known_face_names = [
    "Joe Biden",
    "harshit"
]
face_locations = []
face_encodings = []
face_names = []
cap = cv2.VideoCapture(0)
process_this_frame = True

while True :
    ret,frame = cap.read()

    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        # print(face_locations)

        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        print(len(face_encodings))
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(image_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(image_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            print(name)
            face_names.append(name)
    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        if name != "unknown":
            markAttendance(name)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()