#0 0 2 1 4 3 6 5 8 7 .....
#1 2 3 4 5 6 7 8 9 10 .........

n = int(input('enter a number'))
if n == 1 or n == 2 :
    print('0')
else :
    if n % 2 == 0:
        a = n-3
        print(a)
    else:
        a = n-1
        print(a)