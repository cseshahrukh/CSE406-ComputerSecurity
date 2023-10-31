#author: Md. Shahrukh Islam (1805098)
#implement RSA algorithm for key exchange
# Python3 program Miller-Rabin primality test
import random
import time 
import math
# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
	
	# Initialize result
	res = 1;
	
	# Update x if it is more than or equal to p
	x = x % p;
	while (y > 0):
		
		# If y is odd, multiply
		# x with result
		if (y & 1):
			res = (res * x) % p;

		# y must be even now
		y = y>>1; # y = y/2
		x = (x * x) % p;
	
	return res;

# n is original number 
# It returns false if n is composite and returns true if n is probably prime. 
# d is an odd number such that d*  2^r = n-1 for some r >= 1
def miillerRabinTest(d, n):
	
	# Pick a random number in [2..n-2]
	# generates a random integer between 1 and n - 4, inclusive.
	a = 2 + random.randint(1, n - 4);

	# from some sites noticed that 2 to n-1 also works fine but not good 
	#a = random.randint(3, n - 2);

	# Compute a^d % n
	# base power mod 
	x = power(a, d, n);

	if (x == 1 or x == n - 1):
		return True;

	# keep doubling d 
	# Keep squaring x while one of the following doesn't happen
	# (a) d does not reach n-1
	# (b) (x^2) % n is not 1
	# (c) (x^2) % n is not n-1
	while (d != n - 1):
		x = (x * x) % n
		d *= 2

		if (x == 1):
			return False
		
		# only case of prime 
		if (x == n - 1):
			return True

	# Return composite
	return False;


# It returns false if n is composite and returns true if n is probably prime. 
# k is an input parameter that determines accuracy level. Higher value of k indicates more accuracy.
def isPrime( n, k):
	
    #k is iteration parameter
	# Corner cases
    # 1 and 4 are not prime and are corner cases of miller-rabin test

    
	if (n <= 1 or n == 4):
		return False;
    #2 and 3 are prime 
	if (n <= 3):
		return True;

	# Find r such that n =2^d * r + 1 for some r >= 1 
    # n - 1 = 2^d * r
    # we need the r
	d = n - 1;
	
    # divides the variable d by 2 as long as d is divisible by 2
	while (d % 2 == 0):
		d //= 2;
    # now I have the value of r in the place of variable d

	# Iterate given number of 'k' times
    # return false if n is composite and return true if n is probably prime
    # if one is false then sure that it is composite and if true then probably prime not sure 100%
	for i in range(k):
		if (miillerRabinTest(d, n) == False):
			return False;

	return True;


def generate_prime(k):
    """
    Generate a prime number 'p' with at least 'k' bits where p is prime. 
    """
    iteration=4
    while True:
        p = random.getrandbits(k) | (1 << (k - 1)) | 1  # Generate a random odd number with k bits

        if isPrime(p, iteration):
            return p
        

def setKeys():
    publicKey=0
    privateKey=0
    n=0
    bits=10
    #generate two prime numbers of bits bits

    p1=generate_prime(bits)
    p2=generate_prime(bits)
    #p1!=p2
    while(p1==p2):
        p2=generate_prime(bits-1)

    print('P1 is ',p1)
    print('P2 is ',p2)
    n=p1*p2
    phi=(p1-1)*(p2-1)
    e=2

    #print('Before gcd 1')
    #generate a random number e such that 1<e<phi and gcd(e,phi)=1
    while True:
        e=random.randint(2,phi-1)
        if math.gcd(e,phi)==1:
            break
        #e=e+1
    #print('After gcd 1')


    #generate a random number d such that 1<d<phi and e*d=1 mod phi
    d=0

    #print('Before Inverse Modulo')
    while True:
        d=random.randint(1,phi)
        if (e*d)%phi==1:
            break 
    #print('After Inverse Modulo')
    publicKey=e
    privateKey=d
    return publicKey,privateKey,n

#This actually encrypt the number
def encrypt(message,publicKey,n):
    #encrypt the message using the public key
    cipher=power(message,publicKey,n)
    
    return cipher

#Encrypt the message
def encryptMsg(message,publicKey,n):
    #encrypt the message using the public key
    encryptedMsg=[]
    print('In encryptMsg msg is ',message)
    for i in message:
        encryptedMsg.append(encrypt(ord(i),publicKey,n))
	
    return encryptedMsg

#This actually decrypt the number
def decrypt(cipher,privateKey,n):
    #decrypt the cipher using the private key
    message=power(cipher,privateKey,n)
    return message

#Decrypt the message
def decryptMsg(cipher,privateKey,n):
    #decrypt the cipher using the private key
    #decryptedMsg=[]
    decryptedMsg=''

    for i in cipher:
        #decryptedMsg.append(chr(decrypt(privateKey,n,i)))
        decryptedMsg+=chr(decrypt(i,privateKey,n))

    return decryptedMsg 

#Driver code
if __name__ == "__main__":
    #generate public and private keys
    publicKey,privateKey,n=setKeys()

    #publicKey, privateKey, n =  5, 24509, 30997
    print("Public Key: ",publicKey)
    print("Private Key: ",privateKey)
    print("n: ",n)

    #message to be encrypted
    message="Hello World"
    print("Message: ",message)

    #encrypt the message
    cipher=encryptMsg(message, publicKey, n)
    print("Cipher: ",cipher)

    #decrypt the cipher
    decryptedMsg=decryptMsg(cipher, privateKey, n)
    print("Decrypted Message: ",decryptedMsg)
