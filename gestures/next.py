# 👈

import mediapipe as mp
from gestures.helpers.vector import *
from gestures.helpers.finger_folded import three_fingers_folded_index_unfolded
import config

lm = mp.solutions.hands.HandLandmark

MIN_DIST = config.POINT_MIN_DIST


def gesture_is_next(gesture, multi_handedness_label):
    ok_three_excl_index = three_fingers_folded_index_unfolded(gesture)
    # Index finger is closer to the left side than the wrist
    return ok_three_excl_index and gesture[lm.INDEX_FINGER_TIP].x - gesture[lm.WRIST].x > MIN_DIST
