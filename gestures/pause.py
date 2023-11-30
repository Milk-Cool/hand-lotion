# ✋

from gestures.helpers.vector import *
from gestures.helpers.length import *
import mediapipe as mp

lm = mp.solutions.hands.HandLandmark

MIN_WIDTH = 0.2

def gesture_is_pause(gesture, multi_handedness_label):
    finger1 = get_vector(gesture, lm.INDEX_FINGER_MCP, lm.INDEX_FINGER_TIP)
    finger2 = get_vector(gesture, lm.MIDDLE_FINGER_MCP, lm.MIDDLE_FINGER_TIP)
    finger3 = get_vector(gesture, lm.RING_FINGER_MCP, lm.RING_FINGER_TIP)
    finger4 = get_vector(gesture, lm.PINKY_MCP, lm.PINKY_TIP)

    ok_ang = (
        is_small_angle(finger1, finger2)
        and is_small_angle(finger2, finger3)
        and is_small_angle(finger3, finger4)
    )
    ok_orient = ((multi_handedness_label == "Right" and gesture[lm.THUMB_TIP].x < gesture[lm.PINKY_TIP].x) 
        or (multi_handedness_label == "Left" and gesture[lm.THUMB_TIP].x > gesture[lm.PINKY_TIP].x))
    ok_width = math.hypot(abs(gesture[lm.PINKY_MCP].x - gesture[lm.INDEX_FINGER_MCP].x),
        abs(gesture[lm.PINKY_MCP].y - gesture[lm.INDEX_FINGER_MCP].y)) > MIN_WIDTH

    return ok_ang and ok_orient and is_length_normal(finger1, finger2, finger3, finger4, 0.2) and ok_width