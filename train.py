from ultralytics import YOLO

# Load a model
model = YOLO("D:/py/ultralytics/ultralytics/cfg/models/v8/myyolov8n.yaml")  # build a new model from scratch
model = YOLO("D:/py/ultralytics/yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="D:/py/ultralytics/ultralytics/datasets/ExDark.yaml", epochs=300, batch=64)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
#results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
