import os
import time
import dramatiq
from dramatiq.brokers.redis import RedisBroker

from src.job_state import update_job

broker = RedisBroker(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379
)

dramatiq.set_broker(broker)


@dramatiq.actor(queue_name="image")
def image_recognition(job_id):
    update_job(job_id, "image_recognition")

    print(f"[START] image_recognition {job_id}")
    time.sleep(5)

    ocr.send(job_id)


@dramatiq.actor(queue_name="ocr")
def ocr(job_id):
    update_job(job_id, "ocr")

    print(f"[START] OCR {job_id}")
    time.sleep(8)

    llm_reasoning.send(job_id)


@dramatiq.actor(queue_name="llm")
def llm_reasoning(job_id):
    update_job(job_id, "llm_reasoning")

    print(f"[START] LLM reasoning {job_id}")
    time.sleep(4)

    update_job(job_id, "done")

    print(f"[COMPLETE] {job_id}")