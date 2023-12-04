from gestures.helpers.vector import *
from gestures.helpers.length import *
import mediapipe as mp
import config

lm = mp.solutions.hands.HandLandmark

X_ACCURACY = config.FOLD_X_ACCURACY
MIN_LENGTH = config.FOLD_MIN_LENGTH


def single_finger_folded_straight(gesture, mcp, pip, dip, tip):
    return (
        abs(gesture[mcp].x -
            gesture[pip].x) < X_ACCURACY
        and abs(gesture[dip].x - gesture[tip].x) < X_ACCURACY
    )


def single_finger_folded_side(gesture, pip, dip):
    return (
        abs(gesture[pip].x - gesture[dip].x) < X_ACCURACY
    )


def four_fingers_folded(gesture):
    return (
        # Fingers folded, palm parallel to the camera
        single_finger_folded_straight(
            gesture, lm.INDEX_FINGER_MCP, lm.INDEX_FINGER_PIP, lm.INDEX_FINGER_DIP, lm.INDEX_FINGER_TIP)
        and single_finger_folded_straight(gesture, lm.MIDDLE_FINGER_MCP, lm.MIDDLE_FINGER_PIP, lm.MIDDLE_FINGER_DIP, lm.MIDDLE_FINGER_TIP)
        and single_finger_folded_straight(gesture, lm.RING_FINGER_MCP, lm.RING_FINGER_PIP, lm.RING_FINGER_DIP, lm.RING_FINGER_TIP)
        and single_finger_folded_straight(gesture, lm.PINKY_MCP, lm.PINKY_PIP, lm.PINKY_DIP, lm.PINKY_TIP)
    ) or (
        # Fingers folded, palm perpendicular to the camera
        single_finger_folded_side(
            gesture, lm.INDEX_FINGER_PIP, lm.INDEX_FINGER_DIP)
        and single_finger_folded_side(gesture, lm.MIDDLE_FINGER_PIP, lm.MIDDLE_FINGER_DIP)
        and single_finger_folded_side(gesture, lm.RING_FINGER_PIP, lm.RING_FINGER_DIP)
        and single_finger_folded_side(gesture, lm.PINKY_PIP, lm.PINKY_DIP)
    )


def three_fingers_folded_index_unfolded(gesture):
    index_finger = get_vector(
        gesture, lm.INDEX_FINGER_MCP, lm.INDEX_FINGER_DIP)
    return (
        # Index figer unfolded
        is_length_normal_one(index_finger, MIN_LENGTH)
        # Other three fingers folded, palm parallel to the camera
        and single_finger_folded_straight(gesture, lm.MIDDLE_FINGER_MCP, lm.MIDDLE_FINGER_PIP, lm.MIDDLE_FINGER_DIP, lm.MIDDLE_FINGER_TIP)
        and single_finger_folded_straight(gesture, lm.RING_FINGER_MCP, lm.RING_FINGER_PIP, lm.RING_FINGER_DIP, lm.RING_FINGER_TIP)
        and single_finger_folded_straight(gesture, lm.PINKY_MCP, lm.PINKY_PIP, lm.PINKY_DIP, lm.PINKY_TIP)
    )
