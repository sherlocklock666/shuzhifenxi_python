j = 2
N = 10#从2到N
S_N = 0
S_N_list = []#S_N的每次输出值列表

while j <= N:
	M = 1/(j**2-1)
	S_N = S_N + M
	S_N_list.append(S_N)
	j += 1
else:
	print(S_N_list)




