#author: Md. Shahrukh Islam (1805098)
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
# Establish TCP connection with BOB
alice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
alice_socket.connect(('localhost', 9999))

# Step 1: ALICE sends p, g, and ga (mod p) to BOB
# scan k from console 
#k = int(input("Enter the size: "))

#input k from a text file
f = open("inputHellman.txt", "r")
k = int(f.read())
f.close()

p=generate_special_prime(k)

g=calculate_g(p)

#floor division
a=generate_prime(k//2)
A=power(g,a,p)




print('IN ALICE SIDE: p is ', p)
print('IN ALICE SIDE: g is ', g)
print('IN ALICE SIDE: A is ', A)

alice_socket.send(f'{p},{g},{A}'.encode())

# Step 2: ALICE receives gb (mod p) from BOB
B = int(alice_socket.recv(1024).decode())

# Step 3: Compute the shared secret key
#After Bob sending B
sender_end_secret_key=power(B,a,p)
print('IN ALICE SIDE: sender_end_secret_key is ', sender_end_secret_key)
#shared_key = (gb ** a) % p

# Step 4: Inform BOB that ALICE is ready for transmission
alice_socket.send('Ready'.encode())

# Step 5: Encrypt and send the ciphertext to BOB
#aes = AES(shared_key)  # Initialize AES with the shared key
#convert sender_end_secret_key to string
#sender_end_secret_key=bytes(sender_end_secret_key)
#sender_end_secret_key_bytes = sender_end_secret_key.to_bytes(16, byteorder='big')

#AES_key_input(sender_end_secret_key)
sender_end_secret_key=convert_to_string(sender_end_secret_key)
plaintext = 'Hello BOB!'

#input plaintext from a text file
f = open("plaintextInput.txt", "r")
plaintext = f.read()
f.close()

ciphertext = AES_Encryption_Text(plaintext, sender_end_secret_key)
alice_socket.send(ciphertext.encode())

# Close the connection
alice_socket.close()
