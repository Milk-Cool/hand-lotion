from gestures.helpers.length import *
from gestures.helpers.vector import *
from gestures.helpers.finger_folded import four_fingers_folded
import mediapipe as mp
import config

lm = mp.solutions.hands.HandLandmark

MIN_WIDTH = config.THUMBS_MIN_WIDTH
MAX_FING_LENGTH = config.THUMBS_MAX_FING_LENGTH


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
    ok_vis = math.hypot(
        abs(gesture[lm.PINKY_MCP].x - gesture[lm.INDEX_FINGER_MCP].x),
        abs(gesture[lm.PINKY_MCP].y - gesture[lm.INDEX_FINGER_MCP].y)
    ) > MIN_WIDTH
    ok_len = is_length_normal_max(
        finger1, finger2, finger3, finger4, MAX_FING_LENGTH)

    return ok_ang and four_fingers_folded(gesture) and ok_vis and ok_len
