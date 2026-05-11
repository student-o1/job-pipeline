from tasks import image_recognition
import uuid

for i in range(3):
    job_id = str(uuid.uuid4())
    print(f"Submitting job {job_id}")
    image_recognition.send(job_id)
