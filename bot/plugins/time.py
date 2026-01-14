from datetime import datetime

INFO = "Returns current system time"

def run(_):
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
