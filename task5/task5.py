import pickle
import math
import numpy
from scipy.optimize import minimize

x, y = pickle.load(open('C:/iris.txt', 'rb'), encoding='bytes')

x_new = numpy.zeros((100, 4))
y_new = numpy.zeros((100))

for i in range(0, 100):
    x_new[i] = x[i]
    if y[i] == 0:
        y_new[i] = 1
    else:
        y_new[i] = -1


def func(lambda_l, x, y):
    k = 0
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            k = k + (lambda_l[i] * lambda_l[j] * y[i] * y[j] * skal_pr(x[i], x[j])) / 2
        k = k - lambda_l[i]
    return k


def fit(x, y):
    lambda_l = numpy.zeros((len(y), 1))
    lambda_l = minimize(func, lambda_l, method='nelder-mead',options={'xtol': 1e-8, 'disp': True}).lambda_l
    array = []
    w = y[0] * lambda_l[0] * x[0]
    for i in range(1, len(y)):
        w = w + y[i] * lambda_l[i] * x[i]
    for i in range(len(y)):
        array.append(skal_pr(w, x[i]) - y[i])
    array.sort()
    w0 = array[len(array) / 2]
    return w, w0


def skal_pr(x1, x2):
    z = 0
    for i in range(0, len(x1)):
        z = z + x1[i] * x2[i]
    return z


def sign(x):
    if x >= 0:
        return 1
    else:
        return -1


def sol_func(x,w,w0):
    return sign(skal_pr(w,x) - w0)

def mod(x):
    z = 0
    for i in range(0, len(x)):
        z = z + x[i]
    return z

def CV_leave_one_out_SVM(x, y):
    error = 0
    k = numpy.shape(x)[0]
    for j in range(1, k - 1):
        X_matrix = numpy.vstack((x[0:j], x[j + 1: k]))
        y_matrix = numpy.hstack((y[0:j], y[j + 1: k]))
        t = sol_func(X_matrix,fit(X_matrix,y_matrix)[0],fit(X_matrix,y_matrix)[1])
        if y[j] != t:
            error = error + 1
    return ((k - 2) - error) / (k - 2)

