# 👎

import mediapipe as mp
from gestures.helpers.thumbs_somewhere import is_thumbs_somewhere

lm = mp.solutions.hands.HandLandmark


def gesture_is_down(gesture, multi_handedness_label):
    # Thumb below wrist
    ok_thumb = gesture[lm.THUMB_TIP].y > gesture[lm.WRIST].y

    return is_thumbs_somewhere(gesture) and ok_thumb
