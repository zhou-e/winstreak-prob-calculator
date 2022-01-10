import matplotlib.pyplot as plt
import random

def data_getter():
    obs = int(input('How many observations are in a season/ repetition? '))
    prob = float(input("What's the probability of a success per observation"+ \
        " (<= 1)? "))
    counts = int(input('How many seasons/ repetitions are there? '))
    return (obs, prob, counts)

def one_n(n, p, count):
    lisp = []
    for x in range(count):
        temp = random.choices('10', cum_weights = (p, 1.00), k = n)
        lisp.append(xyzcounter(temp))
    lisp = splitter(lisp)
    return lisp

def xyzcounter(arrv):
    longL = longW = x = y = 0
    if int(arrv[0]):
        x += 1
    else:
        y += 1

    for i in range(1, len(arrv)):
        if arrv[i] == '1' and arrv[i-1] == '1':
            x += 1
        elif arrv[i]  == '0' and arrv[i-1]  == '0':
            y += 1
        else:
            if longL < y:
                longL = y
            if longW < x:
                longW = x
            x = y = 0
    if longL < y:
        longL = y
    if longW < x:
        longW = x
    z = max(longW, longL)
    return (longW, longL ,z)

def splitter(array):
    X = []
    Y = []
    Z = []
    for i in range(len(array)):
        X.append(array[i][0])
        Y.append(array[i][1])
        Z.append(array[i][2])
    return (X, Y, Z)

def god(array, var, xlab, tit):
    temp = []
    freq = []
    for element in array[var]:
        if element not in temp:
            temp.append(element)
            freq.append(array[var].count(element))
    plt.bar(temp, freq, width = 0.3)
    plt.xlabel(xlab)
    plt.ylabel('Frequencies')
    plt.title(tit)
    plt.show()

def joints(array, var1, var2, tit):
    temp1 = []
    temp2 = []
    for i in range(len(array[var1])):
        temp1.append(array[var1][i])
        temp2.append(array[var2][i])
    plt.hist2d(temp1, temp2)
    plt.title(tit)
    plt.show()

def cov_finder(array, var1, var2):
    totCov = totV1 = totV2 = 0
    length = len(array[var1])
    for i in range(length):
        totCov += array[var1][i]*array[var2][i]
        totV1 += array[var1][i]
        totV2 += array[var2][i]
    return totCov/length - totV1/length*totV2/length

def p_lessthan(array, var1, var2):
    temp = 0
    length = len(array[var1])
    for i in range(length):
        if array[var1][i] > array[var2][i]:
            temp += 1
    return temp/length

def exp_x(array):
    temp = 0
    for item in array:
        temp += item
    return temp/len(array)

def prob_streak(array):
    win2 = [0,0]
    win3 = [0,0]
    win4 = [0,0]
    loss2 = [0,0]
    loss3 = [0,0]
    loss4 = [0,0]
    for i in range(len(array)-4):
        if array[i] == array[i+1] == array[i+2] == '1':
            win2[0] += 1
            win2[1] += 1
        elif array[i] == array[i+1] == array[i+2] == '0':
            loss2[0] += 1
            loss2[1] += 1
        elif array[i] == array[i+1] == '1':
            win2[1] += 1
        elif array[i] == array[i+1] == '0':
            loss2[1] += 1

        if array[i] == array[i+1] == array[i+2] == array[i+3] == '1':
            win3[0] += 1
            win3[1] += 1
        elif array[i] == array[i+1] == array[i+2] == array[i+3] == '0':
            loss3[0] += 1
            loss3[1] += 1
        elif array[i] == array[i+1] == array[i+2] == '1':
            win3[1] += 1
        elif array[i] == array[i+1] == array[i+2] == '0':
            loss3[1] += 1

        if array[i] == array[i+1] == array[i+2] == array[i+3] == \
           array[i+4] == '1':
            win4[0] += 1
            win4[1] += 1
        elif array[i] == array[i+1] == array[i+2] == array[i+3] == \
             array[i+4] == '0':
            loss4[0] += 1
            loss4[1] += 1
        elif array[i] == array[i+1] == array[i+2] == array[i+3] == '1':
            win4[1] += 1
        elif array[i] == array[i+1] == array[i+2] == array[i+3] == '0':
            loss4[1] += 1

    if array[-4] == array[-3] == array[-2] == '1':
            win2[0] += 1
            win2[1] += 1
    elif array[-4] == array[-3] == array[-2] == '0':
            loss2[0] += 1
            loss2[1] += 1
    elif array[-4] == array[-3] == '1':
            win2[1] += 1
    elif array[-4] == array[-3] == '0':
            loss2[1] += 1

    if array[-4] == array[-3] == array[-2] == array[-1] == '1':
            win3[0] += 1
            win3[1] += 1
    elif array[-4] == array[-3] == array[-2] == array[-1] == '0':
            loss3[0] += 1
            loss3[1] += 1
    elif array[-4] == array[-3] == array[-2] == '1':
            win3[1] += 1
    elif array[-4] == array[-3] == array[-2] == '0':
            loss3[1] += 1

    if win2[1] == 0:
        win2[1] = 1
    if win3[1] == 0:
        win3[1] = 1
    if win4[1] == 0:
        win4[1] = 1
    if loss2[1] == 0:
        loss2[1] = 1
    if loss3[1] == 0:
        loss3[1] = 1
    if loss4[1] == 0:
        loss4[1] = 1

    return (win2[0]/win2[1], win3[0]/win3[1], win4[0]/win4[1], \
        loss2[0]/loss2[1], loss3[0]/loss3[1], loss4[0]/loss4[1])

def sim_depend(n, p, count, p2w, p3w, p4w, p2l, p3l, p4l):
    total = []
    for x in range(count):
        temp = []
        for y in range(n):
            if len(temp) > 3 and temp[-1] == temp[-2] == temp[-3] \
               == temp[-4]:
                if temp[-1] == 0:
                    temp += random.choices('10', cum_weights = \
                        (p4l, 1.00), k = 1)
                else:
                    temp += random.choices('10', cum_weights = \
                        (p4w, 1.00), k = 1)
            elif len(temp) > 2 and temp[-1] == temp[-2] == temp[-3]:
                if temp[-1] == 0:
                    temp += random.choices('10', cum_weights = \
                        (p3l, 1.00), k = 1)
                else:
                    temp += random.choices('10', cum_weights = \
                        (p3w, 1.00), k = 1)
            elif len(temp) > 1 and temp[-1] == temp[-2]:
                if temp[-1] == 0:
                    temp += random.choices('10', cum_weights = \
                        (p2l, 1.00), k = 1)
                else:
                    temp += random.choices('10', cum_weights = \
                        (p2w, 1.00), k = 1)
            else:
                temp += random.choices('10', cum_weights = (p, 1.00), k = 1)
        total.append(xyzcounter(temp))
    total = splitter(total)
    return total
