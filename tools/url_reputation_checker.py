from urllib.parse import urlparse

url = input("URL: ")

parsed = urlparse(url)

suspicious = [
    "login",
    "verify",
    "secure",
    "update",
    "account"
]

print(f"\nDomain: {parsed.netloc}")

for word in suspicious:
    if word in url.lower():
        print(f"Suspicious keyword detected: {word}")

if "@" in url:
    print("Warning: @ detected")

if len(url) > 100:
    print("Warning: Long URL")

print("Analysis complete")