from datetime import datetime

def log_result(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("results/log.txt", "a") as f:
        f.write(f"[{timestamp}] {text}\n")
