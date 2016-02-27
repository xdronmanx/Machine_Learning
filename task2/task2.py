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
    for x in range(0,len(glist)):
        X_neline = numpy.vstack((X_neline,numpy.array((glist[x]))))


    b = numpy.dot(numpy.dot((numpy.linalg.inv(numpy.dot(X_neline.transpose(), X_neline))), X_neline.transpose()), y)
    return b


def TEST(type,X_line,X_polynom,X_neline,list,results,x1,k):

    if type == 1:
        X = X_line
        b = LINE(X)
        y = numpy.dot(X,b)
        error = results - y
    elif type == 2:
        X = X_polynom
        b = POLYNOM(x1,k)
        y = numpy.dot(X,b)
        error = results - y
    elif type == 3:
        X = X_neline
        b = NELINE(list)
        y = numpy.dot(X,b)
        error = results - y
    return abs(error)    
