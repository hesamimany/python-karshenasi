import redis
import rq
from config import REDIS_HOST, REDIS_PORT, REDIS_QUEUE_NAME

# Connect to Redis
redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# Start worker
worker = rq.Worker([REDIS_QUEUE_NAME], connection=redis_conn)
worker.work()
