n1_20 = {
	0 : 0, 1 : 3, 2 : 3, 3 : 5, 4 : 4, 
	5 : 4, 6 : 3, 7 : 5, 8 : 5, 9 : 4,
	10 : 3, 11 : 6, 12 : 6, 13 : 8, 14 : 8, 
	15 : 7, 16 : 7, 17 : 9, 18 : 8, 19 : 8,
}

n10 = {
	20 : 6, 30 : 6, 
	40 : 5, 50 : 5,
	60 : 5, 70 : 7, 
	80 : 6, 90 : 6,
}

thousand = 8
hundred = 7

def sum1_20(n: int) -> int:
	return n1_20[n]

def sum20_100(n: int) -> int:
	return n10[n - n%10] + n1_20[n%10]

def sum1_100(n: int) -> int:
	return sum1_20(n) if 0 <= n < 20 else sum20_100(n)

def sum100_1000(n: int) -> int:
	ex_and = 3 if n%100 else 0
	return n1_20[n//100] + hundred + ex_and + sum1_100(n%100)

def sum1_1000(n: int) -> int:
	return sum1_100(n) if n < 100 else sum100_1000(n)

def sum1000_M(n: int) -> int:
	return sum1_1000(n//1000) + thousand + sum1_1000(n%1000)

def sum1_M(n: int) -> int:
	return sum1000_M(n) if n >= 1000 else sum1_1000(n)

s, f = map(int, input().split())

sum1 = 0
for i in range(s, f+1):
	sum1 += sum1_M(i)
print(sum1)





