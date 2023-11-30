# 👎

import mediapipe as mp
from gestures.helpers.thumbs_somewhere import *

def gesture_is_down(gesture, multi_handedness_label):
    ok_thumb = gesture[lm.THUMB_TIP].y > gesture[lm.WRIST].y

    return is_thumbs_somewhere(gesture) and ok_thumb