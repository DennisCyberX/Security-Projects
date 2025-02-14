
---

### **3. Caesar Cipher Decoder**
#### `Caesar-Cipher-Decoder/caesar_decoder.py`
```python
def caesar_decoder(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            plaintext += chr((ord(char) - base - shift_amount) % 26 + base)
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")
    shift = int(input("Enter shift value: "))
    print("Decoded text:", caesar_decoder(ciphertext, shift))
