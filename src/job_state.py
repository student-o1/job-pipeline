import os
import time
import redis

# track state
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True # python string
)


def create_job(job_id: str):
    r.hset(f"job:{job_id}", mapping={
        "status": "pending",
        "created_at": str(time.time()),
        "updated_at": str(time.time()),
    })

# only gets rung by worker
def update_job(job_id: str, status: str):
    r.hset(f"job:{job_id}", mapping={
        "status": status,
        "updated_at": str(time.time()),
    })


def get_job(job_id: str):
    return r.hgetall(f"job:{job_id}")