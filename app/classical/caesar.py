class CaesarCipher:
    @staticmethod
    def encrypt(plaintext: str, shift: int = 3, alphabet: str = None) -> str:
        """Encrypt plaintext using Caesar cipher."""
        if alphabet is None:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        result = []
        for char in plaintext:
            if char.lower() in alphabet:
                is_upper = char.isupper()
                idx = alphabet.index(char.lower())
                new_idx = (idx + shift) % len(alphabet)
                new_char = alphabet[new_idx]
                result.append(new_char.upper() if is_upper else new_char)
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def decrypt(ciphertext: str, shift: int = 3, alphabet: str = None) -> str:
        """Decrypt ciphertext using Caesar cipher."""
        return CaesarCipher.encrypt(ciphertext, -shift, alphabet)