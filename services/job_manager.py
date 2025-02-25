import requests
from config import EXPRESS_UPDATE_URL

def update_job_status(job_id: str, status: str, log_message: str, result_path: str = None):
    """
    Calls the Express update endpoint to update the job status.
    """
    payload = {
        "job_id": job_id,
        "status": status,
        "logMessage": log_message
    }
    if result_path:
        payload["resultPath"] = result_path

    try:
        response = requests.post(EXPRESS_UPDATE_URL, json=payload)
        response.raise_for_status()
        print(f"Updated job {job_id} to status '{status}'")
    except Exception as e:
        print(f"Error updating job status for job {job_id}: {e}")
