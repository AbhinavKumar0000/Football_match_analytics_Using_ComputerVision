from ultralytics import YOLO
import cv2
import numpy as np
import math
import cvzone

model = YOLO("models/best.pt")

results = model.predict("input_video_file/B1606b0e6_1 (18).mp4",save=True)

# # Process and print the results
# for result in results:
#     print(result)
#     print("============================")
#     for box in result.boxes:
#         print(box)