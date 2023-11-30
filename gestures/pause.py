# ✋

from gestures.helpers.vector import *
import mediapipe as mp

lm = mp.solutions.hands.HandLandmark

MIN_FINGER_LENGTH = 0.2
MIN_WIDTH = 0.1

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
    ok_length = (
        math.hypot(finger1[0], finger1[1]) > MIN_FINGER_LENGTH
        and math.hypot(finger2[0], finger2[1]) > MIN_FINGER_LENGTH
        and math.hypot(finger3[0], finger3[1]) > MIN_FINGER_LENGTH
        and math.hypot(finger4[0], finger4[1]) > MIN_FINGER_LENGTH
    )
    ok_width = math.hypot(abs(gesture[lm.PINKY_MCP].x - gesture[lm.INDEX_FINGER_MCP].x),
        abs(gesture[lm.PINKY_MCP].y - gesture[lm.INDEX_FINGER_MCP].y)) > MIN_WIDTH

    return ok_ang and ok_orient and ok_length and ok_width