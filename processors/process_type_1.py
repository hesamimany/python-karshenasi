import time
from services.job_manager import update_job_status

def process_file(job_id: str, file_path: str):
    """Example processing function."""
    import asyncio  # Required for async DB updates

    # Start processing
    asyncio.run(update_job_status(job_id, "processing", "Processing started..."))
    
    time.sleep(5)  # Simulate processing delay
    
    # Finish processing
    asyncio.run(update_job_status(job_id, "done", "Processing completed!"))
