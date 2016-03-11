import pickle
import math
import numpy
import random
import sklearn.ensemble as sk
from sklearn.cross_validation import cross_val_score

x, y = pickle.load(open('C:/iris.txt', 'rb'), encoding='bytes')


def i_dj(y):
    zero = 0
    one = 0
    two = 0
    for x in range(0, len(y)):
        if y[x] == 0:
            zero = zero + 1
        elif y[x] == 1:
            one = one + 1
        elif y[x] == 2:
            two = two + 1
    i = zero * (one + two) + one * (zero + two) + two * (zero + one)
    return i / ((zero + one + two) ** 2)


def entrop(y):
    zero = 0
    one = 0
    two = 0
    for x in range(0, len(y)):
        if y[x] == 0:
            zero = zero + 1
        elif y[x] == 1:
            one = one + 1
        elif y[x] == 2:
            two = two + 1
    Pr_z = zero / (zero + one + two)
    Pr_o = one / (zero + one + two)
    Pr_t = two / (zero + one + two)
    if (Pr_z != 0) and (Pr_o != 0) and (Pr_t != 0):
        e = Pr_z * math.log2(1 / Pr_z) + Pr_o * math.log2(1 / Pr_o) + Pr_t * math.log2(1 / Pr_t)
        return e
    elif (Pr_z != 0) and (Pr_o != 0) and (Pr_t == 0):
        e = Pr_z * math.log2(1 / Pr_z) + Pr_o * math.log2(1 / Pr_o)
        return e
    elif (Pr_z != 0) and (Pr_o == 0) and (Pr_t != 0):
        e = Pr_z * math.log2(1 / Pr_z) + Pr_t * math.log2(1 / Pr_t)
        return e
    elif (Pr_z != 0) and (Pr_o == 0) and (Pr_t == 0):
        e = Pr_z * math.log2(1 / Pr_z)
        return e
    elif (Pr_z == 0) and (Pr_o != 0) and (Pr_t != 0):
        e = Pr_o * math.log2(1 / Pr_o) + Pr_t * math.log2(1 / Pr_t)
        return e
    elif (Pr_z == 0) and (Pr_o != 0) and (Pr_t == 0):
        e = Pr_o * math.log2(1 / Pr_o)
        return e
    elif (Pr_z == 0) and (Pr_o == 0) and (Pr_t != 0):
        e = Pr_t * math.log2(1 / Pr_t)
        return e


def gain(y, y1, y2, type):
    if type == 1:
        gain = entrop(y) - (len(y1) / len(y)) * entrop(y1) - (len(y2) / len(y)) * entrop(y2)
        return gain
    elif type == 2:
        gain = i_dj(y) - (len(y1) / len(y)) * i_dj(y1) - (len(y2) / len(y)) * i_dj(y2)
        return gain


def CART(x, y):
    c = 0
    I = 0
    J = 0
    for j in range(0, x.shape[1]):
        for i in range(0, len(x)):
            y1_test = []
            y2_test = []
            for k in range(0, len(x)):
                if x[k][j] >= x[i][j]:
                    y1_test = y1_test + [y[k]]
                if x[k][j] < x[i][j]:
                    y2_test = y2_test + [y[k]]
            if (len(y1_test) != 0) and (len(y2_test) != 0) and ((gain(y, y1_test, y2_test, 1)) > c):
                I = i
                J = j
                c = gain(y, y1_test, y2_test, 1)
    counter = True
    for i in range(0, len(x) - 1):
        if x[i][J] != x[i + 1][J]:
            counter = False
    if counter == True:
        return False
    else:
        return I, J


def TREE(x, y, v):
    if CART(x,y) == False:
        return y[0]
    else:
        y1_index = []
        y2_index = []
        y_left = []
        y_right = []
        i_c,j_c = CART(x, y)
        for i in range(0, len(x)):
            if x[i][j_c] >= x[i_c][j_c]:
                y1_index = y1_index + [i]
                y_left = y_left + [y[i]]
            if x[i][j_c] < x[i_c][j_c]:
                y2_index = y2_index + [i]
                y_right = y_right + [y[i]]
        l_index_0 = y1_index[0]
        x_left = x[l_index_0]
        for i in range(1, len(y1_index)):
            x_left = numpy.vstack((x_left, x[y1_index[i]]))
        r_index_0 = y2_index[0]
        x_right = x[r_index_0]
        for i in range(1, len(y2_index)):
            x_right = numpy.vstack((x_right, x[y2_index[i]]))
        counter_left = True
        for i in range(0, len(y_left) - 1):
            if y_left[i] != y_left[i + 1]:
                counter_left = False
        counter_right = True
        for i in range(0, len(y_right) - 1):
            if y_right[i] != y_right[i + 1]:
                counter_right = False
        if (v[j_c] >= x[i_c][j_c]) and (counter_left == True):
            return y_left[0]
        elif (v[j_c] < x[i_c][j_c]) and (counter_right == True):
            return y_right[0]
        elif (v[j_c] >= x[i_c][j_c]) and (counter_left != True):
            return TREE(x_left, y_left, v)
        elif (v[j_c] < x[i_c][j_c]) and (counter_right != True):
            return TREE(x_right, y_right, v)


def CV_leave_one_out_tree(x, y):
    error = 0
    k = numpy.shape(x)[0]
    for j in range(1, k - 1):
        X_matrix = numpy.vstack((x[0:j], x[j + 1: k]))
        y_matrix = numpy.hstack((y[0:j], y[j + 1: k]))
        t = TREE(X_matrix, y_matrix, x[j])
        if y[j] != t:
            error = error + 1
    return ((k - 2) - error) / (k - 2)


def Random_Forest(x, y, n, m, v, k):
    zero = 0
    one = 0
    two = 0
    for t in range(0, k):
        z = random.randint(0, len(x) - 1)
        y1 = [y[z]]
        x1 = x[z]
        for i in range(0, n - 1):
            z = random.randint(0, len(x) - 1)
            x1 = numpy.vstack((x1, x[z]))
            y1 = y1 + [y[z]]
        a = random.randint(0, numpy.shape(x)[1] - 1)
        x2 = x1[:, a]
        v1 = [v[a]]
        for i in range(0, m - 1):
            a = random.randint(0, numpy.shape(x)[1] - 1)
            x2 = numpy.vstack((x2, x1[:, a]))
            v1 = v1 + [v[a]]
        x2 = x2.transpose()
        answer = TREE(x2, y1, v1)
        if answer == 0:
            zero = zero + 1
        elif answer == 1:
            one = one + 1
        elif answer == 2:
            two = two + 1
    type = max(one, two, zero)
    if type == zero:
        return 0
    elif type == one:
        return 1
    elif type == two:
        return 2


def CV_leave_one_out_random_forest(x, y, m, z):
    error = 0
    k = numpy.shape(x)[0]
    for j in range(1, k - 1):
        X_matrix = numpy.vstack((x[0:j], x[j + 1: k]))
        y_matrix = numpy.hstack((y[0:j], y[j + 1: k]))
        t = Random_Forest(X_matrix, y_matrix, 150, m, x[j], z)
        if y[j] != t:
            error = error + 1
    return ((k - 2) - error) / (k - 2)


def grid_search(x, y):
    M = 0
    Z = 0
    cv = 0
    for z in range(0, 20):
        a = CV_leave_one_out_random_forest(x, y, 4, z)
        if a > cv:
            cv = a
            Z = z
    cv = 0
    for m in range(0, 4):
        a = CV_leave_one_out_random_forest(x, y, m, Z)
        if a > cv:
            cv = a
            M = m
    return M, Z

random_forest = sk.RandomForestClassifier()
scores = cross_val_score(random_forest, x, y)
print(scores.mean())
print(CV_leave_one_out_random_forest(x,y,4,5))

#Grid search показал, что лучше всего строить 5 деревьев, на основе 4 фич
#Кросс-валидация моей реализации очень близка к кросс-валидации стандратной реализации
