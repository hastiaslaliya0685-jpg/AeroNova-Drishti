
from ultralytics import YOLO
import argparse, json

def predict(weights, source, out):
    model = YOLO(weights)
    results = model(source)
    detections = []
    for r in results:
        for box in r.boxes:
            detections.append({
                "class": int(box.cls[0]),
                "confidence": float(box.conf[0]),
                "bbox": box.xyxy[0].tolist()
            })
    with open(out, "w") as f:
        json.dump(detections, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--out", default="preds.json")
    args = parser.parse_args()
    predict(args.weights, args.source, args.out)
