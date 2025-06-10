from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

class RSACrypto:
    @staticmethod
    def generate_keys():
        """Generate RSA key pair."""
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return public_key, private_key

    @staticmethod
    def encrypt(text: str, public_key: bytes) -> str:
        """Encrypt text with RSA public key."""
        rsa_key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        encrypted = cipher.encrypt(text.encode())
        return base64.b64encode(encrypted).decode()

    @staticmethod
    def decrypt(encrypted_text: str, private_key: bytes) -> str:
        """Decrypt text with RSA private key."""
        rsa_key = RSA.import_key(private_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        decrypted = cipher.decrypt(base64.b64decode(encrypted_text))
        return decrypted.decode()

    @staticmethod
    def sign_file(file_path: str, private_key: bytes) -> str:
        """Sign a file with RSA private key."""
        with open(file_path, 'rb') as f:
            data = f.read()
        key = RSA.import_key(private_key)
        h = SHA256.new(data)
        signature = pkcs1_15.new(key).sign(h)
        return base64.b64encode(signature).decode()

    @staticmethod
    def verify_file(file_path: str, signature: str, public_key: bytes) -> bool:
        """Verify a file signature with RSA public key."""
        with open(file_path, 'rb') as f:
            data = f.read()
        key = RSA.import_key(public_key)
        h = SHA256.new(data)
        try:
            pkcs1_15.new(key).verify(h, base64.b64decode(signature))
            return True
        except (ValueError, TypeError):
            return False