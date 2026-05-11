# Job Pipeline
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
```

## Mental Model
enqueue_job.py = customer placing order
Redis = order board where all orders get placed
worker = kitchen chef who processes the orders

## 