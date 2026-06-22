import hashlib

text = input("Text: ")

print("\nMD5")
print(hashlib.md5(text.encode()).hexdigest())

print("\nSHA1")
print(hashlib.sha1(text.encode()).hexdigest())

print("\nSHA256")
print(hashlib.sha256(text.encode()).hexdigest())