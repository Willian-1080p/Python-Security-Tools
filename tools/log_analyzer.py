import sys

if len(sys.argv) < 2:
    print("Usage: python log_analyzer.py logfile.log")
    exit()

logfile = sys.argv[1]

keywords = [
    "failed",
    "denied",
    "error",
    "unauthorized",
    "login failed"
]

with open(logfile, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
        for keyword in keywords:
            if keyword.lower() in line.lower():
                print(line.strip())
                break