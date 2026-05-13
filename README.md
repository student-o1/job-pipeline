# Job Pipeline

- [X] Base functionality
- [X] FastAPI
- [X] Seperated Queues
- [X] Seperated Worker Container per Queue
- [X] Save job status in Redis
- [X] Get status from FastAPI endpoint
- [ ] Vue.js Frontend

## CMDs
**Local:**
```sh
redis-server
dramatiq tasks
python producer.py
```

**Docker:**
```sh
docker compose up --build
python src/enqueue_job.py
curl -X POST http://localhost:8000/jobs
curl http://localhost:8000/jobs/{job_id}
```

## Mental Model
enqueue_job.py = customer placing order

Redis = order board where all orders get placed

worker = kitchen chef who processes the orders

## Technical Model
A new job is started by the producer, and Dramatiq places a message into Redis. Redis acts as a message broker (queue) between the producer and the workers.

Worker processes run in the background and continuously listen for new messages in Redis. As soon as a job appears in the queue, one available worker pick it up and processes it.

True Parallelism?
