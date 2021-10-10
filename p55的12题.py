# m = -0.5

import math

x = 0.5
y = math.exp(2*x)-1-2*x-2*x*x
a = []
b = []

while  abs(y) > 0.001 :
	e = math.exp(2*x)
	N = x-3*(e-1-2*x-2*x*x)/(2*e-2-4*x)
	a.append(N)
	y = e-1-2*x-2*x*x
	b.append(y)
	x = N
else:
	print(f"迭代函数的值为:{a}")
	print(f"f(x)的值为:{b}")


