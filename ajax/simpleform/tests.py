"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

# from django.test import TestCase


# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)

import datetime
from datetime import datetime, timedelta, date

start = datetime.strptime('2012-08-08 03:30', "%Y-%m-%d %H:%M")
end = datetime.strptime('2012-08-11 03:00', "%Y-%m-%d %H:%M")
enda = datetime.strptime('2012-08-09 14:00', "%Y-%m-%d %H:%M")
endb = datetime.strptime('2012-08-09 14:00', "%Y-%m-%d %H:%M")
endc = datetime.strptime('2012-08-10 14:00', "%Y-%m-%d %H:%M")


# go = True
# while go:
# 	if start <= end-timedelta(hours=1):
# 		print start
# 		start = start+timedelta(hours=1)
# 	else:
# 		go = False

times = set([])
testSort = []

times.update([datetime.date(end)])
testSort.append(start.strftime("%x"))

times.update([datetime.date(enda)])
testSort.append(end.strftime("%x"))

times.update([datetime.date(endb)])
testSort.append(enda.strftime("%x"))

times.update([datetime.date(endc)])
testSort.append(endb.strftime("%x"))

for i in times:
	print i.day

import math
print math.fabs(-1)

something = end - start
somethingelse = start - end
print something.seconds
print somethingelse.seconds

print testSort
print sorted(testSort)

print sorted(times)

adate = date(1986, 05, 30)
bdate = date.today()

age = bdate - adate
print age.days/365.25

from random import randint

zero = 0
one = 0

for i in range(0,100):
	x = randint(0,1)
	if x == 0:
		zero += 1
	else:
		one += 1
print zero
print one


testDict = {'Var1': 'Is', 'Var2': 'Foos', 'Var3': 'Changes'}
testDict2 = {'Var1': 'Changed', 'Var2': 'Foos', 'Var3': 'Happen'}

a = set(testDict.items()) - set(testDict2.items())
changes = []
for i in a:
	changes.append(i[0])
print "Changed %s." % changes
