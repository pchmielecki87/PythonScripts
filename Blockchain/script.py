import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import ecdsa

# Provided data
keys_hex = [
    "68544020247570407220244063724074",
    "54684020247570407220244063724074",
    "54684020247570407220244063727440"
]
hash_correct = "f28fe539655fd6f7275a09b7c3508a3f81573fc42827ce34ddf1ec8d5c2421c3"
encrypted_message_hex = "876b4e970c3516f333bcf5f16d546a87aaeea5588ead29d213557efc1903997e"
iv_hex = "656e6372797074696f6e496e74566563"

# Step 1: Identify the correct symmetric key
def find_correct_key(keys_hex, hash_correct):
    for key_hex in keys_hex:
        key_bytes = bytes.fromhex(key_hex)
        hash = hashlib.sha256(key_bytes).hexdigest()
        if hash == hash_correct:
            return key_hex
    return None

correct_key_hex = find_correct_key(keys_hex, hash_correct)

# Step 2: Decrypt the AES-128 encrypted message
def decrypt_message(key_hex, iv_hex, encrypted_message_hex):
    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)
    encrypted_message = bytes.fromhex(encrypted_message_hex)
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()
    
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_message = unpadder.update(decrypted_message) + unpadder.finalize()
    
    return decrypted_message

decrypted_message = decrypt_message(correct_key_hex, iv_hex, encrypted_message_hex)

# Step 3: Generate Asymmetric Elliptic Curve Key-Pair
sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
vk = sk.verifying_key

# Step 4: Generate a Digital Signature
signature = sk.sign(decrypted_message)

# Output results
print("1. Digital Signature:", signature.hex())
print("2. Key-pair Parameters: SECP256k1")
print("3. Asymmetric Public Key:", vk.to_string().hex())