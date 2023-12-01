from gestures.helpers.vector import *
from gestures.helpers.length import *
import mediapipe as mp

lm = mp.solutions.hands.HandLandmark

X_ACCURACY = 0.2
MIN_LENGTH = 0.2

# TODO: remove code duplication
def four_fingers_folded(gesture):
    return (
        (
            abs(gesture[lm.INDEX_FINGER_MCP].x - gesture[lm.INDEX_FINGER_PIP].x) < X_ACCURACY
            and abs(gesture[lm.INDEX_FINGER_DIP].x - gesture[lm.INDEX_FINGER_TIP].x) < X_ACCURACY
        )
        and (
            abs(gesture[lm.MIDDLE_FINGER_MCP].x - gesture[lm.MIDDLE_FINGER_PIP].x) < X_ACCURACY
            and abs(gesture[lm.MIDDLE_FINGER_DIP].x - gesture[lm.MIDDLE_FINGER_TIP].x) < X_ACCURACY
        )
        and (
            abs(gesture[lm.RING_FINGER_MCP].x - gesture[lm.RING_FINGER_PIP].x) < X_ACCURACY
            and abs(gesture[lm.RING_FINGER_DIP].x - gesture[lm.RING_FINGER_TIP].x) < X_ACCURACY
        )
        and (
            abs(gesture[lm.PINKY_MCP].x - gesture[lm.PINKY_PIP].x) < X_ACCURACY
            and abs(gesture[lm.PINKY_DIP].x - gesture[lm.PINKY_TIP].x) < X_ACCURACY
        )
    ) or (
        (
            abs(gesture[lm.INDEX_FINGER_PIP].x - gesture[lm.INDEX_FINGER_DIP].x) < X_ACCURACY
        )
        and (
            abs(gesture[lm.MIDDLE_FINGER_PIP].x - gesture[lm.MIDDLE_FINGER_DIP].x) < X_ACCURACY
        )
        and (
            abs(gesture[lm.RING_FINGER_PIP].x - gesture[lm.RING_FINGER_DIP].x) < X_ACCURACY
        )
        and (
            abs(gesture[lm.PINKY_PIP].x - gesture[lm.PINKY_DIP].x) < X_ACCURACY
        )
    )

def three_fingers_folded_index_unfolded(gesture):
    index_finger = get_vector(gesture, lm.INDEX_FINGER_MCP, lm.INDEX_FINGER_DIP)
    return (
        is_length_normal_one(index_finger, MIN_LENGTH)
        and (
            abs(gesture[lm.MIDDLE_FINGER_MCP].x - gesture[lm.MIDDLE_FINGER_PIP].x) < X_ACCURACY
            and abs(gesture[lm.MIDDLE_FINGER_DIP].x - gesture[lm.MIDDLE_FINGER_TIP].x) < X_ACCURACY
        )
        and (
            abs(gesture[lm.RING_FINGER_MCP].x - gesture[lm.RING_FINGER_PIP].x) < X_ACCURACY
            and abs(gesture[lm.RING_FINGER_DIP].x - gesture[lm.RING_FINGER_TIP].x) < X_ACCURACY
        )
        and (
            abs(gesture[lm.PINKY_MCP].x - gesture[lm.PINKY_PIP].x) < X_ACCURACY
            and abs(gesture[lm.PINKY_DIP].x - gesture[lm.PINKY_TIP].x) < X_ACCURACY
        )
    )