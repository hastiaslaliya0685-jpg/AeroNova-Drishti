
from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import shutil, uuid

app = FastAPI()
model = YOLO("yolov8n.pt")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    temp_name = f"temp_{uuid.uuid4()}.jpg"
    with open(temp_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = model(temp_name)
    output = []
    for r in results:
        for box in r.boxes:
            output.append({
                "class": int(box.cls[0]),
                "confidence": float(box.conf[0]),
                "bbox": box.xyxy[0].tolist()
            })
    return {"detections": output}
