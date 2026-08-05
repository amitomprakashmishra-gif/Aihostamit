from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    image_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # यहाँ AI मॉडल (LivePortrait / MuseTalk आदि) चलाया जाएगा
    output_video = os.path.join(OUTPUT_DIR, "output.mp4")

    # फिलहाल डेमो के लिए
    with open(output_video, "wb") as f:
        f.write(b"")

    return {"video": "/download/output.mp4"}

@app.get("/download/{filename}")
async def download(filename: str):
    return FileResponse(os.path.join(OUTPUT_DIR, filename))
