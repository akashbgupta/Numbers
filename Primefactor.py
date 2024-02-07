def factors(n):
    return [x for x in range(1, n+1) if n % x == 0]
def isprime(n):
    return len(factors(n)) == 2
def primefactors(n):
    return list(filter(isprime, factors(n)))


# def prime_factors(n):
 #   factors = []
    # Divide by 2 until it's odd
  #  while n % 2 == 0:
   #     factors.append(2)
    #    n = n // 2

    # Divide by odd numbers starting from 3
   # for i in range(3, int(n ** 0.5) + 1, 2):
    #    while n % i == 0:
     #       factors.append(i)
      #      n = n // i

    # If the remaining number is a prime greater than 2
#    if n > 2:
 #       factors.append(n)
#
 #   return factors


def primefactorization(n):
    n = int(n)
    f = primefactors(n)
    if isprime(n):
        return str(n)
    else:
        return str(f[0]) + "*" + str(primefactorization(n//f[0]))

def shell():
    print("Welcome to the Prime factorization program. Please enter your number")

    while True:

        print(">>>", end=" ")
        number = input()

        if number == "quit":
            break
        if not number.isdigit() or int(number) < 0:
            print("Please enter a non negative number")
        else:
            print(primefactorization(number))


if __name__ == '__main__':
    shell()


