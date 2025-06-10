from app.modern.rsa import RSACrypto
import os

def test_rsa_encrypt_decrypt():
    public_key, private_key = RSACrypto.generate_keys()
    plaintext = "Hello World"
    encrypted = RSACrypto.encrypt(plaintext, public_key)
    decrypted = RSACrypto.decrypt(encrypted, private_key)
    assert decrypted == plaintext

def test_rsa_with_name():
    public_key, private_key = RSACrypto.generate_keys()
    plaintext = "JohnSmith"
    encrypted = RSACrypto.encrypt(plaintext, public_key)
    decrypted = RSACrypto.decrypt(encrypted, private_key)
    assert decrypted == plaintext

def test_rsa_sign_verify_file():
    test_file = "JohnSmith.txt"
    with open(test_file, 'w') as f:
        f.write("Test content for signing")
    
    public_key, private_key = RSACrypto.generate_keys()
    signature = RSACrypto.sign_file(test_file, private_key)
    assert RSACrypto.verify_file(test_file, signature, public_key) is True
    
    # Tamper with file
    with open(test_file, 'a') as f:
        f.write("modified")
    assert RSACrypto.verify_file(test_file, signature, public_key) is False
    os.remove(test_file)