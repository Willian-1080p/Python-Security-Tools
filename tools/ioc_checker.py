import re

ioc = input("IOC: ")

patterns = {
    "IP": r"^(\d{1,3}\.){3}\d{1,3}$",
    "Domain": r"^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "MD5": r"^[a-fA-F0-9]{32}$",
    "SHA1": r"^[a-fA-F0-9]{40}$",
    "SHA256": r"^[a-fA-F0-9]{64}$"
}

found = False

for name, pattern in patterns.items():
    if re.match(pattern, ioc):
        print(f"Detected: {name}")
        found = True

if not found:
    print("Unknown IOC")