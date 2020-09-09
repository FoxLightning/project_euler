def factor(n: int) -> int:
	f = 1
	for i in range(1, n+1):
		f *= i
	return f

def sum1(n: int) -> int:
	ans = 0
	for num in str(n):
		ans += int(num)
	return ans


print(sum1(factor(int(input()))))
