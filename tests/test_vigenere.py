from app.classical.vigenere import VigenereCipher

def test_vigenere_encrypt_default():
    assert VigenereCipher.encrypt("Hello World") == "Jyffq Zqfbu"

def test_vigenere_decrypt_default():
    assert VigenereCipher.decrypt("Jyffq Zqfbu") == "Hello World"

def test_vigenere_custom_keyword():
    assert VigenereCipher.encrypt("Hello World", "secret") == "Zincq Gvtxk"
    assert VigenereCipher.decrypt("Zincq Gvtxk", "secret") == "Hello World"

def test_vigenere_with_name():
    assert VigenereCipher.encrypt("JohnSmith") == "LvaxXqkad"
    assert VigenereCipher.decrypt("LvaxXqkad") == "JohnSmith"