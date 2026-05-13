import uuid

from fastapi import FastAPI

from src.tasks import image_recognition

app = FastAPI()


@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())

    image_recognition.send(job_id)

    return {
        "message": "job submitted",
        "job_id": job_id,
    }