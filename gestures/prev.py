# 👉

import mediapipe as mp
from gestures.helpers.vector import *
from gestures.helpers.finger_folded import three_fingers_folded_index_unfolded

lm = mp.solutions.hands.HandLandmark

def gesture_is_prev(gesture, multi_handedness_label):
    ok_three_excl_index = three_fingers_folded_index_unfolded(gesture)
    return ok_three_excl_index and gesture[lm.INDEX_FINGER_TIP].x < gesture[lm.WRIST].x