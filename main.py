import streamlit as st
from app.classical.caesar import CaesarCipher
from app.classical.vigenere import VigenereCipher
from app.modern.sha256 import SHA256Hash
from app.modern.rsa import RSACrypto
import base64

st.title("Cryptography Lab Tool")

# Session state for RSA keys
if 'rsa_keys' not in st.session_state:
    st.session_state.rsa_keys = RSACrypto.generate_keys()

# Sidebar navigation
algorithm = st.sidebar.selectbox(
    "Select Algorithm",
    ["Caesar Cipher", "Vigenère Cipher", "SHA-256 Hash", "RSA Encryption"]
)

if algorithm == "Caesar Cipher":
    st.header("Caesar Cipher")
    operation = st.radio("Operation", ["Encrypt", "Decrypt"])
    text = st.text_area("Text")
    col1, col2 = st.columns(2)
    with col1:
        shift = st.number_input("Shift", min_value=1, max_value=25, value=3)
    with col2:
        custom_alphabet = st.text_input("Custom Alphabet (optional)", 
                                      value='abcdefghijklmnopqrstuvwxyz')
    
    if st.button("Execute"):
        if operation == "Encrypt":
            result = CaesarCipher.encrypt(text, shift, custom_alphabet if custom_alphabet else None)
        else:
            result = CaesarCipher.decrypt(text, shift, custom_alphabet if custom_alphabet else None)
        st.text_area("Result", result)

elif algorithm == "Vigenère Cipher":
    st.header("Vigenère Cipher")
    operation = st.radio("Operation", ["Encrypt", "Decrypt"])
    text = st.text_area("Text")
    keyword = st.text_input("Keyword (default: cryptolab)", value="cryptolab")
    
    if st.button("Execute"):
        if operation == "Encrypt":
            result = VigenereCipher.encrypt(text, keyword)
        else:
            result = VigenereCipher.decrypt(text, keyword)
        st.text_area("Result", result)

elif algorithm == "SHA-256 Hash":
    st.header("SHA-256 Hash")
    option = st.radio("Hash", ["Text", "File"])
    
    if option == "Text":
        text = st.text_area("Text to hash")
        if st.button("Hash Text"):
            result = SHA256Hash.hash_text(text)
            st.text_area("Hash Result", result)
    else:
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file and st.button("Hash File"):
            with open("temp_file.txt", "wb") as f:
                f.write(uploaded_file.getbuffer())
            result = SHA256Hash.hash_file("temp_file.txt")
            st.text_area("Hash Result", result)

elif algorithm == "RSA Encryption":
    st.header("RSA Encryption")
    operation = st.radio("Operation", ["Encrypt/Decrypt", "Sign/Verify File"])
    
    if operation == "Encrypt/Decrypt":
        sub_op = st.radio("Action", ["Encrypt", "Decrypt"])
        text = st.text_area("Text")
        
        if sub_op == "Encrypt":
            if st.button("Encrypt"):
                result = RSACrypto.encrypt(text, st.session_state.rsa_keys[0])
                st.text_area("Encrypted Result", result)
        else:
            if st.button("Decrypt"):
                try:
                    result = RSACrypto.decrypt(text, st.session_state.rsa_keys[1])
                    st.text_area("Decrypted Result", result)
                except:
                    st.error("Decryption failed - invalid input or key mismatch")
        
        st.text_area("Public Key", st.session_state.rsa_keys[0].decode())
        st.text_area("Private Key", st.session_state.rsa_keys[1].decode())
        
        if st.button("Generate New Keys"):
            st.session_state.rsa_keys = RSACrypto.generate_keys()
            st.experimental_rerun()
    
    else:  # Sign/Verify
        sub_op = st.radio("Action", ["Sign", "Verify"])
        uploaded_file = st.file_uploader("Choose a file")
        
        if sub_op == "Sign" and uploaded_file and st.button("Sign"):
            with open("temp_file.txt", "wb") as f:
                f.write(uploaded_file.getbuffer())
            signature = RSACrypto.sign_file("temp_file.txt", st.session_state.rsa_keys[1])
            st.text_area("Digital Signature", signature)
        
        elif sub_op == "Verify" and uploaded_file and st.button("Verify"):
            signature = st.text_area("Enter signature to verify")
            if signature:
                with open("temp_file.txt", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                is_valid = RSACrypto.verify_file(
                    "temp_file.txt", signature, st.session_state.rsa_keys[0])
                st.success("Signature is valid" if is_valid else "Signature is invalid")