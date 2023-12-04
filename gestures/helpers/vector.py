import numpy as np
import math
import config

SMALL_ANGLE = config.V_SMALL_ANGLE
VERY_BIG_ANGLE = config.V_VERY_BIG_ANGLE
# Everything in between is just a "big angle"


# Get normalized vector (x, y from 0 to 1)
def get_norm_vector(vector):
    return vector / np.linalg.norm(vector)


# Get angle between vectors
def get_angle(v1, v2):
    v1, v2 = get_norm_vector(v1), get_norm_vector(v2)
    return np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0))


# Get angle between vectors in degrees
def get_angle_deg(v1, v2):
    return get_angle(v1, v2) * (180 / math.pi)


# Get vector of two points on a palm
def get_vector(landmarks, i1, i2):
    return np.array([landmarks[i1].x - landmarks[i2].x, landmarks[i1].y - landmarks[i2].y])


def is_small_angle(v1, v2):
    return abs(get_angle_deg(v1, v2)) < SMALL_ANGLE


def is_big_angle(v1, v2):
    return abs(get_angle_deg(v1, v2)) > SMALL_ANGLE


def is_very_big_angle(v1, v2):
    return abs(get_angle_deg(v1, v2)) > VERY_BIG_ANGLE
