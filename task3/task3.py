import pickle
import math
import numpy
from sklearn.neighbors import KNeighborsClassifier

x, y = pickle.load(open('C:/iris.txt', 'rb'), encoding='bytes')


def S_EVKLIDA(list1, list2):
    a = 0
    for x in range(0, len(list1)):
        a = a + (list1[x] - list2[x]) ** 2
    a = math.sqrt(a)
    return a


def S_MON(list1, list2):
    a = 0
    for x in range(0, len(list1)):
        a = a + abs(list1[x] - list2[x])
    return a


def kNN(v, x, k, metrica_type):
    s = []
    index = []
    if metrica_type == 0:
        for i in range(0, len(x)):
            s = s + [S_EVKLIDA(v, x[i])]
    elif metrica_type == 1:
        for i in range(0, len(x)):
            s = s + [S_MON(v, x[i])]
    for b in range(0, k):
        m = min(s)
        for i in range(0, len(s)):
            if (len(index) < b + 1) and (s[i] == m):
                index = index + [i]
                s.pop(i)
    zero = 0
    one = 0
    two = 0
    for x in range(0, len(index)):
        if y[index[x]] == 0:
            zero = zero + 1
        elif y[index[x]] == 1:
            one = one + 1
        elif y[index[x]] == 2:
            two = two + 1
    type = max(one, two, zero)
    if type == zero:
        return 0
    elif type == one:
        return 1
    elif type == two:
        return 2


def CV_leave_one_out(x, l, y, type):
    error = 0
    k = numpy.shape(x)[0]
    for j in range(1, k - 1):
        X_matrix = numpy.vstack((x[0:j], x[j + 1: k]))
        if type == 0:
            t = kNN(x[j], X_matrix, l, 0)
        elif type == 1:
            t = kNN(x[j], X_matrix, l, 1)
        if y[j] != t:
            error = error + 1
    return ((k - 2) - error) / (k - 2)


def Grid_Search(x, y):
    c = 0
    for j in range(0, 100):
        if CV_leave_one_out(x, j, y, 0) > c:
            c = CV_leave_one_out(x, j, y, 0)
            m = j
    return m


print(CV_leave_one_out(x, 11, y, 0))
kNN1 = KNeighborsClassifier(n_neighbors=3)
kNN1.fit(x, y)
print(kNN1.score(x, y))
print(Grid_Search(x, y))
