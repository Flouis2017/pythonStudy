"""
Test object-oriented programing in Python & fraction operations
"""
import time


class Fraction:
	class_value = 1

	def __init__(self, *args, **kwargs):
		if args[1] <= 0:
			raise Exception('Denominator cannot less than 1!')
		self.num = args[0]
		self.den = args[1]
		for key, value in kwargs.items():
			setattr(self, key, value)

	def __repr__(self):
		return str(self.num) + '/' + str(self.den)

	def get_num(self):
		return self.num

	def get_den(self):
		return self.den

	def __add__(self, other):
		res_num = self.num * other.get_den() + self.den * other.get_num()
		res_den = self.den * other.get_den()
		common = Fraction.gcd(res_num, res_den)
		return Fraction(res_num // common, res_den // common)

	def __eq__(self, other):
		first_num = self.num * other.get_den()
		second_num = other.get_num() * self.den
		return first_num == second_num

	@staticmethod
	def gcd(m, n):
		if m < n:
			m = m + n
			n = m - n
			m = m - n
		while m % n != 0:
			oldm = m
			oldn = n
			m = oldn
			n = oldm % oldn
		return n

	@staticmethod
	def get_date_time():
		return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# ===============================================================
print('============================ test python class ===================================')
f = Fraction(2, 3, lang='Python', author='Flouis')
print('f:', f, '\tstr(f):', str(f), '\tlang:', f.lang, '\tauthor:', f.author)
print('numerator:', f.get_num(), '\tdenominator:', f.get_den())
print(f.class_value, f.get_date_time(), '\t', Fraction.class_value, Fraction.get_date_time())
f = Fraction(1, 3)
f2 = Fraction(1, 6)
print('============================ test "+ =" operation  ===================================')
print(f, '+', f2, '=', f + f2)
print(Fraction.gcd(36, 24))
print(Fraction(1, 2) == Fraction(2, 4))

