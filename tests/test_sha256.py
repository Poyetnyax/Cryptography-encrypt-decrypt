from app.modern.sha256 import SHA256Hash
import os

def test_sha256_hash_text():
    assert SHA256Hash.hash_text("Hello World") == \
        "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
    assert SHA256Hash.hash_text("JohnSmith") == \
        "61b64cebb3979b1a206e1a1dd279e5a9a4d4c1d7a0e9f1a1a0a1a0a1a0a1a0a1"

def test_sha256_hash_file():
    test_file = "JohnSmith.txt"
    with open(test_file, 'w') as f:
        f.write("Test content for file hashing")
    
    expected_hash = SHA256Hash.hash_text("Test content for file hashing")
    assert SHA256Hash.hash_file(test_file) == expected_hash
    os.remove(test_file)