# hand-lotion
Music control using hand gestures (just like on a Pixel 4)

## Requirements
Python 3
```sh
python -m pip install -r requirements.txt
```
or, on Linux and macOS:
```sh
python3 -m pip install -r requirements.txt
```

## Usage
Launch the `main.py` file. You might need to allow the application to send keystrokes and access your camera if you're on Mac.

## Gestures
* 👎 - volume down
* 👍 - volume up
* ✌️ - mute
* ✋ - pause
* 👉 - next track
* 👈 - previous track

## Recommended environment
For the program to recognize your gestures with the best accuracy, you should keep your hands at around 30-40 cm (15-20 in) from your camera. Also the program might not recognize your gestures if there's not enough light in your room.

## Config
See `config.py`