import datetime

LOG_FILE = "wipe_log.txt"

def log(msg: str):
    """Logs a message to the console and to a file with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {msg}"

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")
    except Exception as e:
        print(f"s Failed to write to log file: {e}")
        