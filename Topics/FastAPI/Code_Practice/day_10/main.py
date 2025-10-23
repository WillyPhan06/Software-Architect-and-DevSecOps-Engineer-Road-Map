from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as f:
        f.write(message + "\n")

@app.post("/send-notification/")
def send_notification(background_tasks: BackgroundTasks, email: str):
    background_tasks.add_task(write_log, f"Send notification to {email}")
    return {"message": "Notification scheduled"}
