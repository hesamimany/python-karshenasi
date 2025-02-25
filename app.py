from fastapi import FastAPI
from services.redis_queue import enqueue_job

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "OK"}

@app.post("/enqueue")
def enqueue(job_id: str, file_path: str, process_type: str):
    enqueue_job(job_id, file_path, process_type)
    return {"message": "Job enqueued", "job_id": job_id}
