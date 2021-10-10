###以第二问函数式为示例###
import sympy as sp
x = sp.symbols('x')

#定义Newton迭代函数公式
def Newton_fuction(a):
	f = (x**3)/3-x#函数f(x)表达式
	f1 = sp.diff(f, x)
	F = x-f/f1
	value=F.evalf(subs={x:a})
	return value

# 迭代循环
def Value(x0):
	a = x0#初值
	e = 0.5*10**(-8)#容许误差限
	output_list = []#迭代函数的值组成列表
	for i in range(10**4):
		b = Newton_fuction(a)
		output_list.append(b)
		if abs(b-a) < e:
			print(f"在第{i}次迭代结束\n")
			print(f"迭代值列表：\n\t{output_list}")
			break
		else:
			a = b






	



