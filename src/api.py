from fastapi import FastAPI
import uuid

from src.job_state import create_job, get_job
from src.tasks import image_recognition

app = FastAPI()


@app.post("/jobs")
def create_new_job():
    job_id = str(uuid.uuid4())

    create_job(job_id)
    image_recognition.send(job_id)

    return {"job_id": job_id, "status": "submitted"}

@app.get("/jobs/{job_id}")
def status(job_id: str):
    return get_job(job_id)