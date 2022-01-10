from prob_helper import *

quit = 0
depend = input('Would you like to try making an dependent dataset (Y/N)? ')
if depend.lower() == 'y':
    array = input('Please enter a win loss list seperated by'+ \
        'commas (ex. 0, 1, 1, 1, 0, 0, 1, 0, 1) ').split(', ')
    probs = prob_streak(array)
    gottem = data_getter()
    data = sim_depend(gottem[0], gottem[1], gottem[2], probs[0], \
        probs[1], probs[2], probs[3], probs[4], probs[5])

    while quit != 1:
        print('What would you like to do now?')

        print('You can:\n1. Plot the joint distribution from 2 variables in X,'+ \
            ' Y and Z. As well as calculate their covariance and probability' + \
            ' that) one is greater than the other.')

        print('2. Plot marginal distributions of X, Y, and/or Z.')

        print('3. Quit.')

        choice = int(input('What would you like to do (1-3)? '))
        if choice == 1:
            var1 = int(input("What's the first variable you'd like to have"+ \
            " (0 for X, 1 for Y, 2 for Z)? "))
            var2 = int(input("What's the second variable you'd like to have"+ \
            " (0 for X, 1 for Y, 2 for Z)? "))
            tit = input('What do you want as your title? ')
            joints(data, var1, var2, tit)
            print(cov_finder(data, var1, var2))
            lessthan = input('Do you want to find the probability your'+ \
            " first choice is less than your second (Y/N, if not"+ \
            " it'll be the other way around)? ")
            if lessthan.lower() == 'y':
                print(p_lessthan(data, var2, var1))
            else:
                print(p_lessthan(data, var1, var2))

        elif choice == 2:
            keepgraphing = 'Y'
            while keepgraphing.lower() == 'y':
                var = int(input("What variable would you like to have graphed"+ \
                " (0 for X, 1 for Y, 2 for Z)? "))
                xlab = input('What do you want as your x-axis label? ')
                tit = input('What do you want as your title? ')
                god(data, var, xlab, tit)
                keepgraphing = input('Would you like to keep graphing (Y/N)? ')

        elif choice == 3:
            quit = 1

        else:
            print('Please enter a value from 1-4')

quit = 0

while quit != 1:
    change = input('Would you like to make a new set of data (Y/N)? ')
    if change.lower() == 'y':
        gottem = data_getter()
        obs, prob, counts = gottem[0], gottem[1], gottem[2]

    data = one_n(obs, prob, counts)
    print('What would you like to do now?')

    print('You can:\n1. Plot the joint distribution from 2 variables in X,'+ \
        ' Y and Z. As well as calculate their covariance and probability' + \
        ' that) one is greater than the other.')

    print('2. Plot marginal distributions of X, Y, and/or Z.')

    print('3. See how the (joint) distributions of X, Y, and/or Z'+ \
        ' changes with a fixed n or p (with the other varying).')

    print('4. Quit.')

    choice = int(input('What would you like to do (1-4)? '))
    if choice == 1:
        var1 = int(input("What's the first variable you'd like to have"+ \
        " (0 for X, 1 for Y, 2 for Z)? "))
        var2 = int(input("What's the second variable you'd like to have"+ \
        " (0 for X, 1 for Y, 2 for Z)? "))
        tit = input('What do you want as your title? ')
        joints(data, var1, var2, tit)
        print(cov_finder(data, var1, var2))
        lessthan = input('Do you want to find the probability your'+ \
        " first choice is less than your second (Y/N, if not"+ \
        " it'll be the other way around)? ")
        if lessthan.lower() == 'y':
            print(p_lessthan(data, var2, var1))
        else:
            print(p_lessthan(data, var1, var2))

    elif choice == 2:
        keepgraphing = 'Y'
        while keepgraphing.lower() == 'y':
            var = int(input("What variable would you like to have graphed"+ \
            " (0 for X, 1 for Y, 2 for Z)? "))
            xlab = input('What do you want as your x-axis label? ')
            tit = input('What do you want as your title? ')
            god(data, var, xlab, tit)
            keepgraphing = input('Would you like to keep graphing (Y/N)? ')

    elif choice == 3:
        varChange = input('What variable (n or p) would you like to'+ \
            ' change? ')
        change = input('Would you like to change your orignial data (Y/N)? ')
        if change.lower() == 'y':
            gottem = data_getter()
            obs, prob, counts = gottem[0], gottem[1], gottem[2]
            data = one_n(obs, prob, counts)

        print('This is E(X) currently: %f'%exp_x(data[0]))

        keepgoing = 'Y'
        while keepgoing.lower() == 'y':
            if varChange.lower() == 'n':
                newObs = int(input('What number should new n be? '))
                data = one_n(newObs, prob, counts)
            else:
                newProb = int(input('What number should new p be? '))
                data = one_n(obs, newProb, counts)

            joint = input('Would you like to do a joint distribution (Y/N)? ')
            if joint.lower() == 'y':
                var1 = int(input("What's the first variable you'd like"+ \
                " to have (0 for X, 1 for Y, 2 for Z)? "))
                var2 = int(input("What's the second variable you'd like"+ \
                " to have (0 for X, 1 for Y, 2 for Z)? "))
                tit = input('What do you want as your title? ')
                joints(data, var1, var2, tit)
                print(cov_finder(data, var1, var2))
                lessthan = input('Do you want to find the probability your'+ \
                " first choice is less than your second (Y/N, if not"+ \
                " it'll be the other way around)? ")
                if lessthan.lower() == 'y':
                    print(p_lessthan(data, var2, var1))
                else:
                    print(p_lessthan(data, var1, var2))

            print('This is E(X): %f'%exp_x(data[0]))

            keepgoing = input('Would you like to keep going (Y/N)? ')

    elif choice == 4:
        quit = 1

    else:
        print('Please enter a value from 1-4')
