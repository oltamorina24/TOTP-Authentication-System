from datetime import datetime

def write_log(username, result):
    with open("logs.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} | USER: {username} | RESULT: {result}\n")