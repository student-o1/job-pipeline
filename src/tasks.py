import os
import time
import dramatiq
from dramatiq.brokers.redis import RedisBroker

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")

broker = RedisBroker(host=REDIS_HOST, port=6379)
dramatiq.set_broker(broker)


@dramatiq.actor
def image_recognition(job_id):
    print(f"[START] image_recognition {job_id}")
    time.sleep(1)
    ocr.send(job_id)


@dramatiq.actor
def ocr(job_id):
    print(f"[START] OCR {job_id}")
    time.sleep(1)
    llm_reasoning.send(job_id)


@dramatiq.actor
def llm_reasoning(job_id):
    print(f"[DONE] LLM reasoning {job_id}")
    time.sleep(1)
    print(f"[COMPLETE] {job_id}")
