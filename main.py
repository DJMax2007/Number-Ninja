print('''
    ============================================
    ============*-Number Machine-*==============
    ============================================''')
print()
print('👍 This Machine uses only WHOLE numbers 👍')
print()
vestos = False
while not vestos:
    n = input('Starting number: ')
    m = input('Last number: ')
    if n.isnumeric() and m.isnumeric():
        vestos = True
        valid = False
        while not valid:
            a = int(n)
            c = int(m)
            if c > a:
                valid = True
                b = c + 1
            else:
                print()
                print('-*Please Last number cannot be smaller than Starting number.*-')
                print()
                void = False
                while not void:
                    Exit = input('Please type "RESTART" to start again or type "EXIT" to quit the program: ')
                    if Exit.upper() == 'RESTART':
                        void = True
                        valid = False
                    elif Exit.upper() == 'EXIT':
                        exit()
                    else:
                        print()
                        print('-*Please check your spelling, you can only "RESTART" OR "EXIT"*-')
                        print()
        retro = False
        while not retro:
            print('Do you want exclude multiples of a certain number?')
            answer = input('Yes/No: ')
            if answer.upper() == 'YES' or answer.upper() == 'Y':
                retro = True
                d = int(input('Which number do you want to remove the multiples of: '))
                list = [i for i in range(a, b) if i % d != 0]
            elif answer.upper() == 'NO' or answer.upper() == 'N':
                retro = True
                retrod = False
                while not retrod:
                    print('Do you want to only include multiple of a certain number?')
                    answer = input('Yes/No: ')
                    if answer.upper() == 'YES' or answer.upper() == 'Y':
                        retrod = True
                        d = int(input('Which number do you want the multiples of: '))
                        list = [i for i in range(a, b) if i % d == 0]
                    elif answer.upper() == 'NO' or answer.upper() == 'N':
                        retrod = True
                        list = [i for i in range(a, b)]
                        break
                    else:
                        print()
                        print('-*It is a yes or no question, u can also use y/n*-')
                        print()
            else:
                print()
                print('-*It is a yes or no question, u can also use y/n*-')
                print()
        rotro = False
        while not rotro:
            print('Do you want exclude prime numbers?')
            answerb = input('Yes/No: ')
            if answerb.upper() == 'YES' or answerb.upper() == 'Y':
                rotro = True
                prime = []
                for i in list:
                    v = 0
                    for y in range(1, i):
                        if i % y == 0:
                            v += 1
                    if v == 1:
                        prime.append(i)
                for i in prime:
                    list.remove(i)
            elif answerb.upper() == 'NO' or answerb.upper() == 'N':
                rotro = True
                retrods = False
                while not retrods:
                    print('Do you want to only include prime numbers?')
                    answerc = input('Yes/No: ')
                    if answerc.upper() == 'YES' or answerc.upper() == 'Y':
                        retrods = True
                        prime = []
                        for i in list:
                            v = 0
                            for y in range(1, i):
                                if i % y == 0:
                                    v += 1
                            if v == 1:
                                prime.append(i)
                        list = prime
                    elif answerc.upper() == 'NO' or answerc.upper() == 'N':
                        retrods = True
                        break
                    else:
                        print()
                        print('-*It is a yes or no question, u can also use y/n*-')
                        print()
            else:
                print()
                print('-*It is a yes or no question, u can also use y/n*-')
                print()
        retrad = False
        while not retrad:
            print()
            print('Type "LIST" to see just the list of numbers.')
            print('Type "LENGTH" to see just how many numbers match your criteria in the given range.')
            print('Type "BOTH" to see both the lict of numbers and how many numbers there are.')
            answerd = input('''==================''')
            if answerd.upper() == 'LIST':
                retrad = True
                for i in list:
                    print(i)
            elif answerd.upper() == 'LENGTH':
                retrad = True
                l = len(list)
                if l == 1:
                    print('There is only', len(list), 'number that is between', a, 'to', c,
                          ' inclusive that meets your criterion.')
                elif l == 0:
                    print('There are 0 numbers that between', a, 'to', c, 'inclusive that meets your criterion.')
                elif l > 1:
                    print('There are only', len(list), 'numbers between', a, 'to', c,
                          'inclusive that meets your criterion.')
            elif answerd.upper() == 'BOTH':
                retrad = True
                print()
                print()
                l = len(list)
                if l == 1:
                    print('There is only', len(list), 'number that is between', a, 'to', c,
                          'inclusive that meets your criterion.')
                elif l == 0:
                    print('There are 0 numbers that between', a, 'to', c, 'inclusive that meets your criterion.')
                elif l > 1:
                    print('There are only', len(list), 'numbers between', a, 'to', c,
                          'inclusive that meets your criterion.')
                print()
                for i in list:
                    print(i)
            else:
                print('-*It is a yes or no question, u can also use y/n*-')
                print()
        voider = False
        while not voider:
            print()
            print('Would you also like the to have the sum of all the numbers in your list?')
            Sum = input('Yes/No: ')
            if Sum.upper() == 'YES' or Sum.upper() == 'Y':
                voider = True
                summ = 0
                for number in list:
                    summ += number
                print('Total sum of numbers between', a, 'to', c, 'inclusive that meets your criterion is', summ)
                print('Thank you')
                exit()
            elif Sum.upper() == 'NO' or Sum.upper() == 'N':
                voider = True
                print()
                print('Thank you')
                exit()
            else:
                print()
                print('-*It is a yes or no question, u can also use y/n*-')
                print()
    else:
        print()
        print('-*It is asking for integers that are whole numbers, letters can be used.*-')
        print()
