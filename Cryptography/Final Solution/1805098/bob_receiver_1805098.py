#author: Md. Shahrukh Islam (1805098)
# pip install bitvector
# pip install numpy
import socket
from AESmain2_1805098 import *
from Diffie_Hellman_1805098 import *

def convert_to_string(n):
    if n == 0:
        return '0'

    digits = []
    while n:
        digits.append(chr(n % 256))
        n //= 256

    return ''.join(reversed(digits))
# Establish TCP connection with ALICE
bob_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bob_socket.bind(('localhost', 9999))
bob_socket.listen(5)
print('Waiting for ALICE to connect...')
conn, addr = bob_socket.accept()
print('ALICE connected.')

# Step 1: BOB receives p, g, and ga (mod p) from ALICE
p, g, A = map(int, conn.recv(1024).decode().split(','))

print('In Bob Side: p is ', p)
print('In Bob Side: g is ', g)
print('In Bob Side: A is ', A)
# Step 2: BOB generates gb (mod p) and sends it back to ALICE
#input k from a text file
f = open("inputHellman.txt", "r")
k = int(f.read())
f.close()
#print('k is ', k)

#k at least k size 
b=generate_prime(k//2)  # Private key of BOB
print('b is ', b)

B=power(g,b,p)

conn.send(str(B).encode())

# Step 3: Compute the shared secret key
receiver_end_secret_key=power(A,b,p)
print('In Bob Side: receiver_end_secret_key is ', receiver_end_secret_key)

receiver_end_secret_key=convert_to_string(receiver_end_secret_key)
#shared_key = (ga ** b) % p

# Step 4: Wait for ALICE to be ready for transmission
conn.recv(1024).decode()

# Step 6: Receive the ciphertext from ALICE
ciphertext = conn.recv(1024).decode()

print('Bob get ciphertext from Alice: ', ciphertext)


plaintext = AES_Decryption_Text(ciphertext, receiver_end_secret_key)

print(f'Decrypted message: {plaintext}')

# Close the connection
conn.close()
