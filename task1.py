import math
import random


def ROZENBROK(list):
    c = 0
    for x in range(0, len(list) - 1):
        c = c + (1 - list[x]) ** 2 + 100 * (list[x + 1] - list[x] ** 2) ** 2
    return c


def GRAD_SPUSK(list, delta, type):
    nextlist = [0] * len(list)
    grad = [0] * len(list)
    grad[0] = -2 + 2 * list[0] - 4 * list[1] * list[0] + 4 * list[0] ** 3
    for i in range(1, len(list) - 1):
        grad[i] = -2 + 2 * list[i] - 4 * list[i + 1] * list[i] + 4 * list[i] ** 3 + 2 * list[i] - 2 * list[
                                                                                                          i - 1] ** 2
    grad[len(list) - 1] = 2 * list[len(list) - 1] - 2 * list[len(list) - 2] ** 2
    for x in range(0, len(list)):
        nextlist[x] = list[x] - delta * grad[x]
    while (abs(ROZENBROK(nextlist) - ROZENBROK(list)) > 0.001) or (MINUS(nextlist, list) > 0.001) or NORMA(grad) > 3:
        if type == 1:
            delta = delta
        elif type == 2:
            delta = delta * 0.99999
        elif type == 3:
            delta = DELTA(list, 10, grad, delta)
        grad[0] = -2 + 2 * nextlist[0] - 4 * nextlist[1] * nextlist[0] + 4 * nextlist[0] ** 3
        for i in range(1, len(nextlist) - 1):
            grad[i] = -2 + 2 * nextlist[i] - 4 * nextlist[i + 1] * nextlist[i] + 4 * nextlist[i] ** 3 + 2 * \
                                                                                                        nextlist[
                                                                                                            i] - 2 * \
                                                                                                                 nextlist[
                                                                                                                     i - 1] ** 2
        grad[len(nextlist) - 1] = (2 * nextlist[len(nextlist) - 1] - 2 * nextlist[len(nextlist) - 2] ** 2)
        for x in range(0, len(list)):
            list[x] = nextlist[x]
        for x in range(0, len(list)):
            nextlist[x] = list[x] - delta * grad[x]
    return nextlist


def DELTA(list, n, grad, delta):
    helplist = [0] * len(list)
    c = 100000000000
    for x in range(0, n):
        delta = delta * random.uniform(0.998,0.999)
        for i in range(0, len(list)):
            helplist[i] = list[i] - delta * grad[i]
        if ROZENBROK(helplist) < c:
            c = ROZENBROK(helplist)
            m = delta
    return m


def NORMA(list):
    a = 0
    for i in range(0, len(list)):
        a = a + list[i] ** 2
    a = math.sqrt(a)
    return a


def MINUS(list1, list2):
    a = 0
    for x in range(0, len(list1)):
        a = a + (list1[x] - list2[x]) ** 2
    a = math.sqrt(a)
    return a


def MONTE_KARLO(list1, list2, n):
    helplist1 = [0] * len(list1)
    helplist2 = [0] * len(list1)
    for x in range(0, n):
        for i in range(0, len(list1)):
            helplist1[i] = random.randint(list1[i], list2[i])
        if ROZENBROK(helplist1) < ROZENBROK(helplist2):
            helplist2 = helplist1
    return helplist2


list1 = [0, 0, 0, 0]
list2 = [3, 3, 3, 3]
n = 10
print(GRAD_SPUSK(MONTE_KARLO(list1, list2, n), 0.1, 3))
