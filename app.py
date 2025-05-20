import cv2
import mediapipe as mp
import threading
import numpy as np
from tensorflow.keras.models import load_model
import pickle
import pygame
from gtts import gTTS
import pyttsx3

import functions
import text_to_speech

pygame.mixer.init()
engine = pyttsx3.init()

engine.setProperty('rate', 125)    # Speed of speech
engine.setProperty('volume', 1) 

mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose


model=load_model("model.h5")
with open('onehot_encoder_output.pkl',"rb") as file:
    oe=pickle.load(file)

def speech(text):
    engine.say(text)
    engine.runAndWait()

name="mani     "


cap=cv2.VideoCapture(1)
poses={1:"pranamasana",2:"hasta uttanasana",3:"Hastapadasana",4:"Ashwa Sanchalanasana",5:"stickpose",6:"Ashtanga namaskara",7:"cobra",8:"adho mukha svanasana",0:"Nothing"}
count=0
curr_pos=1
status=''
with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
        while curr_pos<=12:
                ret,frame=cap.read()

                image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                image.flags.writeable=False

                results=pose.process(image)
                image.flags.writeable=True
                image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

                mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(245,117,66),thickness=2,circle_radius=2),
                                          mp_drawing.DrawingSpec(color=(245,66,230),thickness=2,circle_radius=2)
                                        )
                l=[]
                if results.pose_landmarks:
                    a= results.pose_landmarks.landmark[0].x
                    b= results.pose_landmarks.landmark[0].y
                    c= results.pose_landmarks.landmark[0].z
                    landmarks=results.pose_landmarks.landmark
                    for i in landmarks:
                        l.extend([i.x-a,i.y-b,i.z-c])

                    l = np.array([l])
                    prediction=model.predict(l)
                    pos = np.argmax(prediction) 
                    cv2.putText(image, f'target pose:{poses[curr_pos]} ', (20, 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)   
                    cv2.putText(image, f'current pose: {poses[pos]}', (20, 40), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)      
                    if pos>8: 
                          pos=11-pos
                          
                    if pos==curr_pos:
                          if pos==1 or pos==11:
                                status=functions.Pranamasana(landmarks)
                          elif pos==2 or pos==10:
                                status=functions.Hastauttanasana(landmarks)
                          elif pos==3 or pose==9:
                                status=functions.Hastapadasana(landmarks)
                          elif pos==4:
                                status=functions.Ashwa_Sanchalanasana_left(landmarks)
                          elif pos==5:
                                status=functions.ashtanga(landmarks)
                          elif pos==6:
                                status=functions.cobra(landmarks)
                          elif pos==7:
                                status=functions.adho_mukha(landmarks)
                          elif pos==8:
                                status=functions.Ashwa_Sanchalanasana_right(landmarks)

                          if status=='perfect':             
                              pygame.mixer.music.load(r"C:\Users\karth\Desktop\TrainWithAI\duolingo_correct.mp3")
                              pygame.mixer.music.play()
                              count+=1
                              curr_pos+=1
                          else:         
                              # Convert text to speech and play it
                              tts_thread = threading.Thread(target=speech, args=(name+status,))
                              tts_thread.start()    
                              cv2.putText(image, f'feedback: {status}', (20, 200), cv2.QT_FONT_NORMAL, 0.7, (255, 255, 255), 2)
                              pass 
             
                cv2.imshow("TrainWithAI",image)
                if cv2.waitKey(40) & 0xFF==ord('q'):
                        break

        cap.release()
        cv2.destroyAllWindows()