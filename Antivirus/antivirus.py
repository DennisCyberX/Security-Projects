
---

### **4. Antivirus**
#### `Antivirus/antivirus.py`
```python
import os
import hashlib

KNOWN_MALICIOUS_HASHES = [
    "e99a18c428cb38d5f260853678922e03",  # Example MD5 hash
]

def scan_file(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    if file_hash in KNOWN_MALICIOUS_HASHES:
        print(f"Malicious file detected: {file_path}")
    else:
        print(f"File is clean: {file_path}")

def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            scan_file(os.path.join(root, file))

if __name__ == "__main__":
    directory_to_scan = input("Enter directory to scan: ")
    scan_directory(directory_to_scan)
