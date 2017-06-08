#Square an integer the hard way
x = 3
ans = 0
itersLeft = x

while (itersLeft != 0):
	ans = ans + abs(x)
	itersLeft = itersLeft - 1
print str(x) + '*' + str(x) + ' = ' + str(ans)
