# ✌️

from gestures.helpers.thumbs_somewhere import *

def gesture_is_mute(gesture, multi_handedness_label):
    finger1 = get_vector(gesture, lm.INDEX_FINGER_PIP, lm.INDEX_FINGER_DIP)
    finger2 = get_vector(gesture, lm.MIDDLE_FINGER_PIP, lm.MIDDLE_FINGER_DIP)
    finger3 = get_vector(gesture, lm.RING_FINGER_PIP, lm.RING_FINGER_DIP)
    finger4 = get_vector(gesture, lm.PINKY_PIP, lm.PINKY_DIP)

    ok_peace = get_angle_deg(finger1, finger2) > 10
    ok_rest_closed = is_very_big_angle(finger2, finger3) and is_small_angle(finger3, finger4)

    return ok_peace and ok_rest_closed