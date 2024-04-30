'''
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
...
...
1x9=9.........9x9=81
'''
for i in range(9):
    for j in range(i+1):
        print('%dx%d=%d'% (j+1,i+1,(j+1)*(i+1)),end=' ')
    print()