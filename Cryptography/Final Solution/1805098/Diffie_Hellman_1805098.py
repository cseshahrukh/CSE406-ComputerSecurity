#author: Md. Shahrukh Islam (1805098)
import random
import time 
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
        

def generate_special_prime(k):
    """
    Generate a prime number 'p' with at least 'k' bits where p and (p-1)/2 are prime.
    """
    iteration=4
    while True:
        p = random.getrandbits(k) | (1 << (k - 1)) | 1  # Generate a random odd number with k bits

        if isPrime(p, iteration) and isPrime((p - 1) // 2, iteration):
            return p

def calculate_g(p):
    """
    Calculate a value 'g' such that 2 <= g < p-1, g^2 % p != 1, and g^((p-1)/2) != 1.
    """
    while True:
        g = random.randint(2, p-2)  # Generate a random value within the range

        if power(g, 2, p) != 1 and power(g, (p-1)//2, p) != 1:
            return g

def main2():
    # Your program logic here
    print("Hello, World!")

    # Number of iterations
    k = 4;

    print("All primes smaller than 100: ")
    for i in range(1,100):
        if (isPrime(i, k)):
            print(i , end=" ");

def mainPrev():
	# scan k from console 
    #k = int(input("Enter the size: "))

    #input k from a text file
    f = open("inputHellman.txt", "r")
    k = int(f.read())
    f.close()
    #print('k is ', k)

    start_time = time.time()
    p=generate_special_prime(k)
    end_time = time.time()
    pTime=end_time-start_time
    #print('p is ', p)

    start_time = time.time()
    g=calculate_g(p)
    end_time = time.time()
    gTime=end_time-start_time
    print('g is ', g)

    start_time = time.time()

    #floor division
    a=generate_prime(k//2)
    end_time = time.time()
    aTime=end_time-start_time
    b=generate_prime(k//2)
    
    print('a is ', a)
    print('b is ', b)

    start_time = time.time()
    A=power(g,a,p)
    end_time = time.time()
    ATime=end_time-start_time

    B=power(g,b,p)
    print('A is ', A)
    print('B is ', B)

    start_time = time.time()
    sender_end_secret_key=power(B,a,p)
    

    receiver_end_secret_key=power(A,b,p)

    end_time = time.time()
    keyTime=end_time-start_time

    
    print('sender_end_secret_key is ', sender_end_secret_key)
    print('receiver_end_secret_key is ', receiver_end_secret_key)
    
    

    if (sender_end_secret_key==receiver_end_secret_key):
        print('sender_end_secret_key and receiver_end_secret_key are equal')
    else:
        print('sender_end_secret_key and receiver_end_secret_key are not equal')


    #print all times in 20 decimal places

    """
    print('pTime is ', format(pTime, '.20f'))
    print('gTime is ', format(gTime, '.20f'))
    print('aTime is ', format(aTime, '.20f'))
    print('ATime is ', format(ATime, '.20f'))
    print('keyTime is ', format(keyTime, '.20f'))
    return pTime, gTime, aTime, ATime, keyTime
    """


    """
    print('pTime is ', pTime)
    print('gTime is ', gTime)
    print('aTime is ', aTime)
    print('ATime is ', ATime)
    print('keyTime is ', keyTime)
    """
    return pTime, gTime, aTime, ATime, keyTime


def main():
    pTime=0
    gTime=0
    aTime=0
    ATime=0
    keyTime=0
    iteration=5
    for i in range(iteration):
        pTemp, gTemp, aTemp, ATemp, keyTemp=mainPrev()
        pTime+=pTemp
        gTime+=gTemp
        aTime+=aTemp
        ATime+=ATemp
        keyTime+=keyTemp
    #mainPrev()
    pTime/=iteration
    gTime/=iteration
    aTime/=iteration
    ATime/=iteration
    keyTime/=iteration

    print('pTime is ', format(pTime, '.20f'))
    print('gTime is ', format(gTime, '.20f'))
    print('aTime is ', format(aTime, '.20f'))
    print('ATime is ', format(ATime, '.20f'))
    print('keyTime is ', format(keyTime, '.20f'))


# Check if this module is being run directly
if __name__ == "__main__":
    # Call the main function
    main()
