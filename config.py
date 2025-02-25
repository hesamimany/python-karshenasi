import os

# Redis Configuration
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_QUEUE_NAME = os.getenv("REDIS_QUEUE_NAME", "file_processing")

# Express Service Update URL
# This is the endpoint in your Express app that handles job updates (e.g., /jobs/update)
EXPRESS_UPDATE_URL = os.getenv("EXPRESS_UPDATE_URL", "http://localhost:3000/api/jobs/update")
