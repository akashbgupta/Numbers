import random
import matplotlib.pyplot as plt

def frequency(trials, flips):
    results = []

    for flip in range(1, flips+1):
        head_count = 0
        tail_count = 0

        for trail in range(1, trials+1):
            result = random.choice([0,1])
            if result == 0:
                head_count += 1
            else:
                tail_count += 1

        results.append((head_count, tail_count))

    return results

def plot_results(results):
    flips = list(range(1, len(results) + 1))
    heads = [result[0] for result in results]
    tails = [result[1] for result in results]

    plt.plot(flips, heads, label='Heads')
    plt.plot(flips, tails, label='Tails')
    plt.xlabel('Number of Flips')
    plt.ylabel('Count')
    plt.title('Heads and Tails Frequency')
    plt.legend()
    plt.show()


def shell():
    print ("Welcome to coin toss frequency calculator. Enter the number of trails and flips")

    while True:
        print("Number of trials:", end=" ")
        trials = input()

        if trials.lower() == "quit":
            break

        print("Number of flips:", end=" ")
        flips = input()

        if flips.lower() == "quit":
            break

        try:
            trials = int(trials)
            flips = int(flips)
            print(frequency(trials, flips))
            plot_results(frequency(trials, flips))
        except ValueError:
            print("Please enter valid integer values for trials and flips.")


if __name__ == '__main__':
    shell()