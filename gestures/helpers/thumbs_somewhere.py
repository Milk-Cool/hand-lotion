from gestures.helpers.vector import *
import mediapipe as mp

lm = mp.solutions.hands.HandLandmark

X_ACCURACY = 0.2
MIN_WIDTH = 0.2

def is_thumbs_somewhere(gesture):
    finger1 = get_vector(gesture, lm.INDEX_FINGER_PIP, lm.INDEX_FINGER_DIP)
    finger2 = get_vector(gesture, lm.MIDDLE_FINGER_PIP, lm.MIDDLE_FINGER_DIP)
    finger3 = get_vector(gesture, lm.RING_FINGER_PIP, lm.RING_FINGER_DIP)
    finger4 = get_vector(gesture, lm.PINKY_PIP, lm.PINKY_DIP)

    ok_ang = (
        is_small_angle(finger1, finger2)
        and is_small_angle(finger2, finger3)
        and is_small_angle(finger3, finger4)
    )
    ok_fing = (
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
    )
    ok_vis = math.hypot(
        abs(gesture[lm.PINKY_MCP].x - gesture[lm.INDEX_FINGER_MCP].x),
        abs(gesture[lm.PINKY_MCP].y - gesture[lm.INDEX_FINGER_MCP].y)
    ) > MIN_WIDTH

    return ok_ang and ok_fing and ok_vis
    