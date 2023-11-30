import math

MIN_FINGER_LENGTH = 0.2

def is_length_normal(finger1, finger2, finger3, finger4):
    return (
        math.hypot(finger1[0], finger1[1]) > MIN_FINGER_LENGTH
        and math.hypot(finger2[0], finger2[1]) > MIN_FINGER_LENGTH
        and math.hypot(finger3[0], finger3[1]) > MIN_FINGER_LENGTH
        and math.hypot(finger4[0], finger4[1]) > MIN_FINGER_LENGTH
    )