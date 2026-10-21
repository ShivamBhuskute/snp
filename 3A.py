
import hashlib

message = "Hello Students"
hash1 = hashlib.sha256(message.encode()).hexdigest()

print("Original Message :", message)
print("SHA-256 Hash     :", hash1)

modified = "Hello Student"
hash2 = hashlib.sha256(modified.encode()).hexdigest()

print("\nModified Message :", modified)
print("SHA-256 Hash     :", hash2)

if hash1 == hash2:
    print("\nMessage Not Modified")
else:
    print("\nMessage Modified")
