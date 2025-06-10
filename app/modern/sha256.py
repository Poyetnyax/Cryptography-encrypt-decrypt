from hashlib import sha256

class SHA256Hash:
    @staticmethod
    def hash_text(text: str) -> str:
        """Generate SHA-256 hash of text."""
        return sha256(text.encode()).hexdigest()

    @staticmethod
    def hash_file(file_path: str) -> str:
        """Generate SHA-256 hash of file content."""
        with open(file_path, 'rb') as f:
            return sha256(f.read()).hexdigest()