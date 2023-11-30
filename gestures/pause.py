# ✋

from gestures.helpers.vector import *
import mediapipe as mp

lm = mp.solutions.hands.HandLandmark

def is_ok(v1, v2):
    return abs(get_angle_deg(v1, v2)) < 10

def gesture_is_pause(gesture, multi_handedness_label):
    finger1 = get_vector(gesture, lm.INDEX_FINGER_MCP, lm.INDEX_FINGER_TIP)
    finger2 = get_vector(gesture, lm.MIDDLE_FINGER_MCP, lm.MIDDLE_FINGER_TIP)
    finger3 = get_vector(gesture, lm.RING_FINGER_MCP, lm.RING_FINGER_TIP)
    finger4 = get_vector(gesture, lm.PINKY_MCP, lm.PINKY_TIP)

    ok_ang = is_ok(finger1, finger2) and is_ok(finger2, finger3) and is_ok(finger3, finger4)
    ok_orient = (multi_handedness_label == "Right" and gesture[lm.THUMB_TIP].x < gesture[lm.PINKY_TIP].x or multi_handedness_label == "Left" and gesture[lm.THUMB_TIP].x > gesture[lm.PINKY_TIP].x)

    return ok_ang and ok_orient