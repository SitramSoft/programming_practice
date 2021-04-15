#Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs (x):
    #ans = ans + 1
    ans = ans
if ans**3 != abs(x):
    print(x, 'is not a perfect cuve')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)
