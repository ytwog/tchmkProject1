import random
import math

N = 10 ** 100


def lab(M):
    res = 0
    for i in range(M):
        a_start = a = random.randint(1, N)
        b_start = b = random.randint(1, N)
        if a < b:
            a, b = b, a
        while b != 0:
            res += 1
            temp = b
            b = a % b
            a = temp
        print("gcd(" + str(a_start) + ", " + str(b_start) + ") = " + str(a))
    return res / M


def teorethical(N):
    return 12 * math.log(2) / math.pi / math.pi * math.log(N) + 1


print("Average: " + str(lab(5)))
print("Teoreth: " + str(teorethical(N)))
