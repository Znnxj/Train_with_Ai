
import cv2
import mediapipe as mp
import numpy as np
import os
import functions
mp_drawing=mp.solutions.drawing_utils
mp_pose=mp.solutions.pose



def angle(a,b,c):
    a=np.array(a)
    b=np.array(b)
    c=np.array(c)
    
    radians=np.arctan2(c[1]-b[1],c[0]-b[0])-np.arctan2(a[1]-b[1],a[0]-b[0])
    angle=np.abs(radians*180.0/np.pi)

    if angle>180:
        angle=360-angle
    return angle



def Pranamasana(landmarks):
    return "perfect"

def Hastauttanasana(landmarks):
    message=[]
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
    hip_x,hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
    knee_x,knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
    ankle_x,ankle_y=landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
    

    if(angle([shoulder_x,shoulder_y],[hip_x,hip_y],[knee_x,knee_y])>120):
        message.append("Bend towards your back")
    if(angle([ankle_x,ankle_y],[knee_x,knee_y],[hip_x,hip_y])<168):
        message.append("Keep your knees stright")
    if not message:
        return "perfect"

    return ' and '.join(message)

def Hastapadasana(landmarks):
    message=[]
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
    hip_x,hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
    knee_x,knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
    ankle_x,ankle_y=landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y

    if(angle([ankle_x,ankle_y],[knee_x,knee_y],[hip_x,hip_y])<168):
        message.append("Keep your knees stright")
    if(angle([shoulder_x,shoulder_y],[hip_x,hip_y],[knee_x,knee_y])>90):
        message.append("Lean forward")

    if not message:
        return "perfect"

    return ' and '.join(message)


def Ashwa_Sanchalanasana_left(landmarks):
    message=[]
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
    r_hip_x,r_hip_y=landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y
    l_hip_x,l_hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
    r_knee_x,r_knee_y=landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y
    l_knee_x,l_knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y    
    l_ankle_x,l_ankle_y=landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
    r_ankle_x,r_ankle_y=landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y

    if(angle([r_ankle_x,r_ankle_y],[r_knee_x,r_knee_y],[r_hip_x,r_hip_y])<120):
        message.append("Lean forward ")
    if(angle([r_knee_x,r_knee_y],[r_hip_x,r_hip_y],[l_knee_x,l_knee_y])<90):
        message.append("Push your hip the ground")
    if(angle([l_hip_x,l_hip_y],[l_knee_x,l_knee_y],[l_ankle_x,l_ankle_y])>=100 or angle([l_hip_x,l_hip_y],[l_knee_x,l_knee_y],[l_ankle_x,l_ankle_y])<=70 ):
        message.append("Keep your left knee parallel to your left ankle")
    
    if not message:
        return "perfect"

    return ' and '.join(message)



def stick_pose(landmarks):
    message=[]
    elbow_x,elbow_y=landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
    wrist_x,wrist_y=landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
    hip_x,hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
    knee_x,knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y

    if(angle([shoulder_x,shoulder_y],[hip_x,hip_y],[knee_x,knee_y])<160):
        message.append("keep you back stright")
    if(angle([shoulder_x,shoulder_y],[elbow_x,elbow_y],[wrist_x,wrist_y])<160):
        message.append("keep you arms stright")
    if not message:
        return "perfect"

    return ' and '.join(message)

def ashtanga(landmarks):
    return "perfect"

def cobra(landmarks):
    message=[]
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
    hip_x,hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
    knee_x,knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
    if(angle([shoulder_x,shoulder_y],[hip_x,hip_y],[knee_x,knee_y])>130):
        message.append("stretch back keeping your head up")
    
    if not message:
        return "perfect"

    return ' and '.join(message)

def adho_mukha(landmarks):
    return "perfect"
    


def Ashwa_Sanchalanasana_right(landmarks):
    message=[]
    shoulder_x,shoulder_y=landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
    l_hip_x,l_hip_y=landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y
    r_hip_x,r_hip_y=landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
    l_knee_x,l_knee_y=landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y
    r_knee_x,r_knee_y=landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y    
    r_ankle_x,r_ankle_y=landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
    l_ankle_x,l_ankle_y=landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y

    if(angle([l_ankle_x,l_ankle_y],[l_knee_x,l_knee_y],[l_hip_x,l_hip_y])<170):
        message.append("Lean forward with a strech in your inner tighs")
    if(angle([l_knee_x,l_knee_y],[l_hip_x,l_hip_y],[r_knee_x,r_knee_y])<150):
        message.append("Push your hip the ground")
    if(angle([r_hip_x,r_hip_y],[r_knee_x,r_knee_y],[r_ankle_x,r_ankle_y])>=95 or angle([l_hip_x,l_hip_y],[l_knee_x,l_knee_y],[l_ankle_x,l_ankle_y])<=75 ):
        message.append("Keep your left knee parallel to your left ankle")
    
    if not message:
        return "perfect"

    return ' and '.join(message)
