def isprime(n):

    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False

    return True

def nextprime(n):
    k  = n+1 #next number

    while True:
        if not isprime(k):      #if number n+1 is not prime, the loop progresses due to not False.
            k +=1               # new number is k+1
        else:                   #if k is prime, then break the look and return k
            break
    return k

def shell():
    print("Welcome to the next prime number calculator!")

    while True:
        print(">>>", end=" ")

        number = input()

        if number.lower() == 'quit':
            break
        try:
            number = int(number)
            if number < 0:
                print("Enter a positive integer!")
            else:
                print(nextprime(number))
        except ValueError:
            print("Please input a number you motherfucker!")

if __name__ == '__main__':
    shell()


