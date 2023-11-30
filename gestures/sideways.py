# 🫸

from gestures.helpers.palm_sideways import *
import mediapipe as mp

lm = mp.solutions.hands.HandLandmark

def gesture_is_sideways(gesture, multi_handedness_label):
    ok_sideways = is_sideways_palm(gesture)

    return ok_sideways