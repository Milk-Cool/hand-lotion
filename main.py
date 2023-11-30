from gestures_controller import GesturesController
from media_controller import MediaController
from time import sleep

gestures_controller = GesturesController()
media_controller = MediaController()

while(True):
    event = gestures_controller.gesture_tick()
    if event == gestures_controller.E_PAUSE:
        media_controller.play_pause()
    elif event == gestures_controller.E_UP:
        media_controller.vol_up()
    elif event == gestures_controller.E_DOWN:
        media_controller.vol_down()
    sleep(0.05)