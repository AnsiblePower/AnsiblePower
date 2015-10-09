import paramiko
from Crypto.PublicKey import RSA

if __name__ == "__main__":
    bits = 2048
    new_key = RSA.generate(bits, e=65537)
    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")
    print public_key


