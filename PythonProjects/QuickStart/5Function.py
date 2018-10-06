
def isPrime(n):
    if( n == 1):
        print("1 is a special Number")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} = {} * {} ".format(n , x , n // x))
            return True
    else:
        print("{} is a prime Number".format(n))
        return True




for n in range(1, 20):
    isPrime(n)



