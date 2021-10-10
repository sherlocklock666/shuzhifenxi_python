#定义求从2到N之和的函数
def Two_to_N(N):
	j = 2
	S_N = 0
	while j <= N:
		M = 1/(j**2-1)
		S_N = S_N + M
		j += 1
	else:
		return S_N

#定义求有效数字和误差的函数
def Effective_numbers(N):
	exact_S_N = 0.5*(1.5-1/N-1/(N+1))
	S_N = Two_to_N(N)
	e = abs(exact_S_N - S_N)
	i = 0
	while e < 0.5*(1/(10**i)):
		i += 1
	else:
		print(f"近似值：{S_N}\t有效位数：{i-1}\t误差值：{e}\n")

#取N为100，10000，1000000的迭代结果
for i in [2, 4, 6]:
	print(f"当N={10**i}时:")
	Effective_numbers(10**i)
