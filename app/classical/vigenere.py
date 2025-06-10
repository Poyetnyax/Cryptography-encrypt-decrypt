class VigenereCipher:
    @staticmethod
    def encrypt(plaintext: str, keyword: str = 'cryptolab') -> str:
        """Encrypt plaintext using Vigenère cipher."""
        key_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
        result = []
        for p_char, k_char in zip(plaintext, key_repeated):
            if p_char.isalpha():
                shift = ord(k_char.lower()) - ord('a')
                if p_char.isupper():
                    result.append(chr((ord(p_char) - ord('A') + shift) % 26 + ord('A')))
                else:
                    result.append(chr((ord(p_char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result.append(p_char)
        return ''.join(result)

    @staticmethod
    def decrypt(ciphertext: str, keyword: str = 'cryptolab') -> str:
        """Decrypt ciphertext using Vigenère cipher."""
        key_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
        result = []
        for c_char, k_char in zip(ciphertext, key_repeated):
            if c_char.isalpha():
                shift = ord(k_char.lower()) - ord('a')
                if c_char.isupper():
                    result.append(chr((ord(c_char) - ord('A') - shift) % 26 + ord('A')))
                else:
                    result.append(chr((ord(c_char) - ord('a') - shift) % 26 + ord('a')))
            else:
                result.append(c_char)
        return ''.join(result)