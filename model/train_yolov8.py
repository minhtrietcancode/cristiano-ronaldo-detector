from ultralytics import YOLO

# Load a pre-trained YOLOv8n model
model = YOLO('yolov8n.pt')

# Define the path to your custom data.yaml
data_yaml_path = '../My First Project.v1i.yolov8/data.yaml'

# Train the model with your custom dataset
# You can adjust epochs, image size (imgsz), and other parameters as needed
results = model.train(data=data_yaml_path, epochs=100, imgsz=640)

# Perform inference on the test set and save results with bounding boxes
inference_results = model.predict(source='../train_test_data/test_data', save=True, conf=0.25)

# You can optionally save the trained model
model.save('my_finetuned_yolov8.pt') 