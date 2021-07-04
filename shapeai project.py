import hashlib

result = hashlib.md5(b"pooja shree").hexdigest()
print(result)

result = hashlib.md5("pooja shree".encode("utf-8")).hexdigest()
print(result)
