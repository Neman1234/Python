from pathlib import Path
from urllib.request import urlretrieve

import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

model_path = Path("hand_landmarker.task")

if not model_path.exists():
    urlretrieve(
        "https://storage.googleapis.com/mediapipe-models/"
        "hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task",
        model_path
    )

image_bgr = cv2.imread("hand.jpg")

if image_bgr is None:
    raise FileNotFoundError("Put a photo named hand.jpg beside this program.")

image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
Options = mp.tasks.vision.HandLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode

options = Options(
    base_options=BaseOptions(model_asset_path=str(model_path)),
    running_mode=RunningMode.IMAGE,
    num_hands=2
)

with HandLandmarker.create_from_options(options) as detector:
    result = detector.detect(mp_image)

height, width, _ = image_rgb.shape

for hand in result.hand_landmarks:
    for point in hand:
        x = int(point.x * width)
        y = int(point.y * height)
        cv2.circle(image_rgb, (x, y), 5, (255, 0, 0), -1)

print("Hands found:", len(result.hand_landmarks))

plt.imshow(image_rgb)
plt.axis("off")
plt.show()
