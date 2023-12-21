import cv2
import mediapipe as mp
import numpy as np
import time
import config

from gestures.down import gesture_is_down
from gestures.mute import gesture_is_mute
from gestures.next import gesture_is_next
from gestures.prev import gesture_is_prev
from gestures.pause import gesture_is_pause
from gestures.up import gesture_is_up


class GesturesController:
    def __init__(self):
        # Gestures
        self.G_NONE = -1
        self.G_DOWN = 0
        self.G_MUTE = 1
        self.G_NEXT = 2
        self.G_PREV = 3
        self.G_PAUSE = 4
        self.G_UP = 5

        # Events
        self.E_NONE = -1
        self.E_DOWN = 0
        self.E_MUTE = 1
        self.E_NEXT = 2
        self.E_PAUSE = 3
        self.E_PREV = 4
        self.E_UP = 5

        # Time to ignore festures for after one was recognized
        self.IGNORE_TIME = config.IGNORE_TIME

        # Time to wait for with repeating gestures (volume up, volume down)
        # Must be greater than IGNORE_TIME
        self.WAIT_TIME = config.WAIT_TIME

        self.last_gesture = self.G_NONE
        self.last_gesture_time = -100
        self.last_gesture_x = -1

        self.detector = mp.solutions.hands.Hands()
        self.cap = cv2.VideoCapture(0)

        self.gestures = [
            [gesture_is_pause, self.E_PAUSE, self.G_PAUSE, 0],
            [gesture_is_mute, self.E_MUTE, self.G_MUTE, 0],
            [gesture_is_next, self.E_NEXT, self.G_NEXT, 0],
            [gesture_is_prev, self.E_PREV, self.G_PREV, 0],
            [gesture_is_up, self.E_UP, self.G_UP, 1],
            [gesture_is_down, self.E_DOWN, self.G_DOWN, 1]
        ]

    def get_camera_image(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        frame = np.fliplr(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

    def get_hands(self, img):
        return self.detector.process(img)

    def get_camera_hands(self):
        return self.get_hands(self.get_camera_image())

    def gesture_tick(self):
        hands = self.get_camera_hands()
        if hands.multi_hand_landmarks is None:
            return

        ctime = time.time()

        if ctime - self.last_gesture_time < self.IGNORE_TIME:
            return self.E_NONE

        for i in range(len(hands.multi_hand_landmarks)):
            args = [hands.multi_hand_landmarks[i].landmark,
                    hands.multi_handedness[i].classification[0].label]
            for gesture in self.gestures:
                if gesture[0](*args):
                    if (
                        gesture[3] == 0 and self.last_gesture != gesture[2]
                        or gesture[3] == 1 and self.last_gesture_time > self.WAIT_TIME
                    ):
                        self.last_gesture = gesture[2]
                        self.last_gesture_time = ctime
                        return gesture[1]
                    return self.E_NONE
            self.last_gesture = self.G_NONE

        return self.E_NONE
