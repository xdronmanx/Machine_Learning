import math


def metrica(x1,x2):
    k = 0
    for i in range(0,len(x1)):
        k = k + (x1[i]-x2[i])**2
        k = math.sqrt(k)
        return k

def claster(x,x1_index,x2_index,p):
    if len(x1_index) != 0:
        array = []
        flag = True
        for i in range(0,len(x1_index)):
            for j in range(0,len(x2_index)):
                if metrica(x[x1_index[i]],x[x2_index[j]]) >= p:
                    flag = False
        if flag == True:
            for i in range(0,len(x1_index)):
                array.append(x1_index[i])
            for j in range(0,len(x2_index)):
                array.append(x2_index[j])
            return True , array
        else:
            return False , 0
    else:
        return x2_index

def div_ierar(x,p):
    index = []
    for i in range(0,len(x)):
        index.append(i)
    array = [[]]
    while (any(index) == False):
        index_array = []
        for i in range(0,len(x)):
            if index[i] != -1:
                if claster(x,index_array,[i],p)[1] == True:
                    index_array.append(i)
                    index[i] = -1

        array.append(index_array)
    return array

def any(index):
    t = True
    for i in range(0,len(index)):
        if index[i] != -1:
            t = False
    return t

def div_k_means(x,k):
    array = [[[]]]
    index_array = [[]]
    for i in range(0,k):
        array.append([x[i]])
        index_array.append([i])
    mass_array = [[]]
    for i in range(0,k):
        mass_array.append([mass_centre(array[i])])
    for i in range(k,len(x)):
        min = 100000
        index = 0
        for j in range(0,k):
            if (metrica(x[i],mass_array[k]) <= min):
                min = metrica(x[i],mass_array[k])
                index = k
        array[index].append(x[i])
        index_array[index].append(i)
    return array





def mass_centre(x):
    m = [0] * len(x[0])
    for i in range(0,len(x)):
        for j in range(0,len(m)):
            m[j] = m[j] + x[i][j]
    for k in range(0,len(m)):
        m[k] = m[k]/len(x)
    return m
