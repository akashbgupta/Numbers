def fibonacci(n, fiblist=None):
    if fiblist is None:
        fiblist = {}

    if n in fiblist:
        return fiblist[n]
    elif n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 2, fiblist) + fibonacci(n - 1, fiblist)

    fiblist[n] = result
    return result

def shell():
    print("Welcome to the Fibonacci Calculator. "
          "Enter the number of the sequence. If you want to quit, type 'quit'")

    fibonacci_values = {}
    while True:
        print(">>>", end=" ")
        entry = input()

        if entry == 'quit':
            break
        if not entry.isdigit() or int(entry) < 0:
            print("Please enter a non-negative integer")
        else:
            n = int(entry)
            if n not in fibonacci_values:
                fibonacci_values[n] = fibonacci(n, fibonacci_values)
            print(f"Fibonacci({n}): {fibonacci_values[n]}")

if __name__ == '__main__':
    shell()


