from pynput.keyboard import Key, Controller

class MediaController:
    def __init__(self):
        self.controller = Controller()

    def press(self, key):
        self.controller.tap(key)
        print(key)
    
    def mute(self):
        self.press(Key.media_volume_mute)
    
    def vol_up(self):
        self.press(Key.media_volume_up)
    
    def vol_down(self):
        self.press(Key.media_volume_down)
    
    def prev(self):
        self.press(Key.media_previous)
    
    def next(self):
        self.press(Key.media_next)
    
    def play_pause(self):
        self.press(Key.media_play_pause)