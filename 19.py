o = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

e = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class DOW:
	def __init__(self):
		self.day = 1
	def __str__(self):
		"""
		return: str object
		"""
		return str(self.day)
	def next_day(self):
		"""
		next day
		"""
		if self.day < 7:
			self.day += 1
		else:
			self.day = 1
	def days(self):
		"""
		return: int object
		"""
		return self.day




def check_manth(month, day):
	for _ in range(month):
		d.next_day()
	return d.days() == 0

def check_year(year, day, monthend=12):
	count = 0
	for n, month in enumerate(year):
		if n == monthend:
			return count
		if check_manth(month, day):
			count += 1
	return count

def extra_year(n: int) -> bool:
	if n % 4 == 0:
		if n % 100 == 0 and n % 400 != 0:
			return False
		return True
	else:
		return False

def check_data(current )
def format(s:str) -> list:
	return s.split("-")[:2]
d = DOW()
s, f = map(format, input().split())

for i in range(1900, 3000):









