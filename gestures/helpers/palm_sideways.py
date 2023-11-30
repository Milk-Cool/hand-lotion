import mediapipe as mp
from gestures.helpers.length import *
from gestures.helpers.vector import *

lm = mp.solutions.hands.HandLandmark

MAX_WIDTH = 0.2

def is_sideways_palm(gesture):
    ok_sideways = abs(gesture[lm.PINKY_TIP].x - gesture[lm.INDEX_FINGER_TIP].x) < MAX_WIDTH
    ok_length = is_length_normal_max(
        get_vector(gesture, lm.INDEX_FINGER_PIP, lm.INDEX_FINGER_DIP),
        get_vector(gesture, lm.MIDDLE_FINGER_PIP, lm.MIDDLE_FINGER_DIP),
        get_vector(gesture, lm.RING_FINGER_PIP, lm.RING_FINGER_DIP),
        get_vector(gesture, lm.PINKY_PIP, lm.PINKY_DIP),
        0.2
    )

    return ok_sideways and ok_length