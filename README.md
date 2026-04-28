# Real-Time Hand Gesture Controller

Control your mouse and media actions using hand gestures with Python, OpenCV, MediaPipe, and PyAutoGUI.

## Features

- Move mouse cursor with your index finger
- Left click with index + middle finger up
- Play/Pause with open hand (all fingers up)
- Mute with middle finger up only
- Skip right with ring finger up only
- Skip left with pinky finger up only
- Adjust volume based on thumb-index pinch distance
- Show instruction image with a keyboard shortcut

## Requirements

- Python 3.9+ (recommended)
- Webcam
- Windows (tested environment)

## Python dependencies

Install required packages:

```bash
pip install opencv-python mediapipe pyautogui
```

## Run

From the project folder:

```bash
python HandGestureControl.py
```

## Keyboard shortcuts (while app is running)

- `q`: Quit the app
- `s`: Save current camera frame to `HandGestureControl.jpg`
- `i`: Open `HandInstructions.png`

## Gesture controls

- **Open hand** (thumb + index + middle + ring + pinky up): Presses `space` (play/pause)
- **Middle finger only**: Presses `volumemute`
- **Index + middle** (ring and pinky down): Left click
- **Ring finger only**: Presses `right` key
- **Pinky only**: Presses `left` key
- **Index up**: Moves mouse pointer to index fingertip position
- **Otherwise**: Uses thumb-index distance to control volume (`volumeup` / `volumedown`)

## Notes

- Some gestures have a cooldown to reduce accidental repeated actions.
- Camera quality, lighting, and background can affect tracking accuracy.
- If controls feel jumpy, improve lighting and keep your hand centered in frame.

## File structure

- `HandGestureControl.py`: Main script
- `HandInstructions.png`: Instruction image shown with `i`
- `HandGestureControl.jpg`: Sample/saved output image

## 🚀 Demo

[![Hand Gesture Demo](https://img.youtube.com/vi/87QTKgbuSko/0.jpg)](https://www.youtube.com/watch?v=87QTKgbuSko)
▶️ Full Demo: https://www.youtube.com/watch?v=87QTKgbuSko



