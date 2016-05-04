import numpy as np
x = np.random.randint(0, 101, size=10)
s = np.sort(x)[::-1]
print(s),
print(np.mean(s))


def sequence(n, pool):
    team = pool
    A = []
    B = []
    for i in range(0, n):
        x = bin(i)[2:]
        c = 0
        for letter in x:
            if letter == '1':
                c += 1

        if c % 2 == 0:
            A.append(team[i])
        else:
            B.append(team[i])

    print(A),
    print(np.mean(A)),
    print(np.mean(team[0::2]))
    print(B),
    print(np.mean(B)),
    print(np.mean(team[1::2]))
    print("Difference using Thue-Morse is %s" % (np.mean(A)-np.mean(B)))
    print("Difference using ordered sequence is %s" % (np.mean(team[0::2])-np.mean(team[1::2])))


sequence(10, list(range(1, 21)))
