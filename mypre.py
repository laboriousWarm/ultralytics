from ultralytics import YOLO
from PIL import  Image
import  cv2
model = YOLO("D:/py/ultralytics/runs/detect/train/weights/best.pt")
model.predict(source="D:/py/ultralytics/ultralytics/datasets/ExDark/test/images/2015_00522.jpg",show=True)
while(True):
    1