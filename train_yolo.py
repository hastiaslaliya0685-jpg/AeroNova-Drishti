
from ultralytics import YOLO
import argparse

def train(data, epochs, imgsz):
    model = YOLO("yolov8n.pt")
    model.train(data=data, epochs=epochs, imgsz=imgsz)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--imgsz", type=int, default=640)
    args = parser.parse_args()
    train(args.data, args.epochs, args.imgsz)
