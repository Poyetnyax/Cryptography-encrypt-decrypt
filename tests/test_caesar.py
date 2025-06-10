from app.classical.caesar import CaesarCipher

def test_caesar_encrypt_default():
    assert CaesarCipher.encrypt("Hello World") == "Khoor Zruog"

def test_caesar_decrypt_default():
    assert CaesarCipher.decrypt("Khoor Zruog") == "Hello World"

def test_caesar_custom_shift():
    assert CaesarCipher.encrypt("Hello World", 5) == "Mjqqt Btwqi"
    assert CaesarCipher.decrypt("Mjqqt Btwqi", 5) == "Hello World"

def test_caesar_custom_alphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    assert CaesarCipher.encrypt("Hello World", 3, alphabet) == "Khoor Zruog"
    assert CaesarCipher.decrypt("Khoor Zruog", 3, alphabet) == "Hello World"

def test_caesar_with_name():
    assert CaesarCipher.encrypt("JohnSmith") == "MrkqVplwk"
    assert CaesarCipher.decrypt("MrkqVplwk") == "JohnSmith"