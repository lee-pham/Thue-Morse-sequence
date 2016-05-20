import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns


def sequence(small, large, size):
    pool = np.sort(np.random.randint(small, large, size))[::-1]
    A = 0
    B = 0
    Aturn = []
    Bturn = []
    Ateam = []
    Bteam = []
    for i in range(0, size):
        x = bin(i)[2:]
        c = 0
        for letter in x:
            if letter == '1':
                c += 1

        if c % 2 == 0:
            A += pool[i]
            Ateam.append(A)
            Aturn.append(i)
        else:
            B += pool[i]
            Bturn.append(i)
            Bteam.append(B)

    plt.figure(1)
    plt.plot(Aturn, Ateam)
    plt.plot(Bturn, Bteam)
    plt.xlabel('Turn')
    plt.ylabel('Team Value')
    plt.title('Thue-Morse Selection Sequence')
    plt.figure(2)
    plt.plot(list(range(0, size))[::2], Ateam)
    plt.plot(list(range(0, size))[1::2], Bteam)
    plt.xlabel('Turn')
    plt.ylabel('Team Value')
    plt.title('Traditional Selection Sequence')
    plt.show()


sequence(0, 100, 22)
