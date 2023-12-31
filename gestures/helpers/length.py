import math


def is_length_normal(finger1, finger2, finger3, finger4, leng):
    # Fingers are long enough (longer than leng)
    return (
        math.hypot(finger1[0], finger1[1]) > leng
        and math.hypot(finger2[0], finger2[1]) > leng
        and math.hypot(finger3[0], finger3[1]) > leng
        and math.hypot(finger4[0], finger4[1]) > leng
    )


def is_length_normal_one(finger, leng):
    # Same thing but for a single finger
    return (
        math.hypot(finger[0], finger[1]) > leng
    )


def is_length_normal_max(finger1, finger2, finger3, finger4, leng):
    # Fingers are short enough (shorter than leng)
    return (
        math.hypot(finger1[0], finger1[1]) < leng
        and math.hypot(finger2[0], finger2[1]) < leng
        and math.hypot(finger3[0], finger3[1]) < leng
        and math.hypot(finger4[0], finger4[1]) < leng
    )
