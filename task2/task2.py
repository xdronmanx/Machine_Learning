import numpy
import math
import random

k = 3
list1 = [8, 1, 3, 4]
list2 = [15, 4, 9, 3]
list3 = [3, 3, 3, 3]
ylist = [5, 5, 5, 9]

line_1 = [1] * k
x1 = numpy.array(list1)
x2 = numpy.array(list2)
x3 = numpy.array(list3)

b = numpy.array(([0] * k))
y = numpy.array(ylist)

test = numpy.array((list1, list2, list3))


def LINE(X_line):
    X_line
    b = numpy.dot(numpy.dot((numpy.linalg.inv(numpy.dot(X_line.transpose(), X_line))), X_line.transpose()), y)
    return b


def POLYNOM(x1, k):
    X_polynom = x1
    for i in range(2, k):
        X_polynom = numpy.vstack((X_polynom, x1 * i))
    X_polynom = numpy.vstack((line_1, X_polynom))
    b = numpy.dot(numpy.dot((numpy.linalg.inv(numpy.dot(X_polynom.transpose(), X_polynom))), X_polynom.transpose()), y)
    return b


def NELINE(list):
    glist = [[]]
    for x in range(len(glist)):
        for i in range(0, x1.size):
            glist[x] = glist[x] + [list[x](x1[i])]
    X_neline = numpy.array((line_1))
    for x in range(0, len(glist)):
        X_neline = numpy.vstack((X_neline, numpy.array((glist[x]))))

    b = numpy.dot(numpy.dot((numpy.linalg.inv(numpy.dot(X_neline.transpose(), X_neline))), X_neline.transpose()), y)
    return b


test = numpy.array((list1, list2, list3))


def CV_k_fold(X, type, k):
    error = 0
    X = numpy.array_split(X, k)
    for j in range(1, k - 1):
        X_matrix = numpy.vstack((X[0:j], X[j + 1, k]))
        if type == 1:
            b = LINE(X_matrix)
            y = numpy.dot(X_matrix, b)
            error = error + abs(numpy.sum(y - X[j]))
        elif type == 2:
            b = POLYNOM(X_matrix, 10)
            y = numpy.dot(X_matrix, b)
            error = error + abs(numpy.sum(y - X[j]))
        elif type == 3:
            b = NELINE(X_matrix)
            y = numpy.dot(X_matrix, b)
            error = error + abs(numpy.sum(y - X[j]))
    return error


def CV_leave_one_out(X, type):
    error = 0
    k = numpy.shape(X)[0]
    X = numpy.array_split(X, k)
    for j in range(1, k):
        X_matrix = numpy.vstack((X[0:j], X[j + 1, k]))
        if type == 1:
            b = LINE(X_matrix)
            y = numpy.dot(X_matrix, b)
            error = error + abs(numpy.sum(y - X[j]))
        elif type == 2:
            b = POLYNOM(X_matrix, 10)
            y = numpy.dot(X_matrix, b)
            error = error + abs(numpy.sum(y - X[j]))
        elif type == 3:
            b = NELINE(X_matrix)
            y = numpy.dot(X_matrix, b)
            error = error + abs(numpy.sum(y - X[j]))
    return error


def COMPARE(X, type, k):
    e1 = CV_k_fold(X, type, k)
    e2 = CV_leave_one_out(X, type)
    print("Ошибка при 1 кросс-валидации :", e1)
    print("Ошибка при 2 кросс-валидации :", e2)
    print("Разница ошибок :", abs(e1 - e2))
