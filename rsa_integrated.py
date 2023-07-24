from rsa import *

def encrypt_rsa(p,q,r,file):
    with open(file,'r') as file1:
        data = file1.read()
    enc_text = rsa_encrypt(p,q,r,data)
    return enc_text

def decrypt_rsa(p,q,r,file):
    dec_text = rsa_decrypt(p,q,r,file)
    return dec_text