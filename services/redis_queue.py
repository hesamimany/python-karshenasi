import redis
import rq
from config import REDIS_HOST, REDIS_PORT, REDIS_QUEUE_NAME

# Connect to Redis
redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# Create a queue
queue = rq.Queue(REDIS_QUEUE_NAME, connection=redis_conn)

def enqueue_job(job_id: str, file_path: str, process_type: str):
    """Enqueues a job for processing."""
    queue.enqueue(f"processors.{process_type}.process_file", job_id, file_path)
