import numpy

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


def LINE(list1, list2, list3):
    X_line = numpy.array((line_1, list1, list2, list3))
    b = numpy.dot(numpy.dot((numpy.linalg.inv(numpy.dot(X_line.transpose(), X_line))), X_line.transpose()), y)
    return b


def POLYNOM(x1, k):
    X_polynom = x1
    for i in range(2, k):
        X_polynom = numpy.vstack((X_polynom, x1 * i))
    X_polynom = numpy.vstack((line_1, X_polynom))
    b = numpy.dot(numpy.dot((numpy.linalg.inv(numpy.dot(X_polynom.transpose(), X_polynom))), X_polynom.transpose()), y)
    return b


def g1(n):
    return n


def g2(n):
    return n + 1


def g3(n):
    return n


def NELINE(g1, g2, g3):
    glist1 = []
    for i in range(0, x1.size):
        glist1 = glist1 + [g1(x1[i])]

    glist2 = []
    for i in range(0, x1.size):
        glist2 = glist2 + [g2(x1[i])]

    glist3 = []
    for i in range(0, x1.size):
        glist3 = glist3 + [g3(x1[i])]

    X_neline = numpy.vstack((line_1, numpy.array((glist1, glist2, glist3))))
    b = numpy.dot(numpy.dot((numpy.linalg.inv(numpy.dot(X_neline.transpose(), X_neline))), X_neline.transpose()), y)
    return b


def TEST(dataset, type, k, g1, g2, g3):
    for x in range(0,len(dataset)):
        X_polynom = dataset[x]
        for i in range(2, k):
            X_polynom = numpy.vstack((X_polynom, dataset[x] * i))
        X_polynom = numpy.vstack((line_1, X_polynom))
        X_line = numpy.array((line_1, list1, list2, list3))
        glist1 = []
        for i in range(0, x1.size):
            glist1 = glist1 + [g1(x1[i])]

        glist2 = []
        for i in range(0, x1.size):
            glist2 = glist2 + [g2(x1[i])]

        glist3 = []
        for i in range(0, x1.size):
            glist3 = glist3 + [g3(x1[i])]

        X_neline = numpy.vstack((line_1, numpy.array((glist1, glist2, glist3))))
        if type == 1:
            X = X_line
            y = numpy.dot(X, LINE(x1))
        elif type == 2:
            X = X_polynom
            y = numpy.dot(X, POLYNOM(x1, k))
        elif type == 3:
            X = X_neline
            y = numpy.dot(X, NELINE(g1, g2, g3))
