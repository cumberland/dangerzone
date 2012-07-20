testword = "123456789"

newTest = testword.strip()
if " " in newTest:
	print "Bad Variable"
else:
	print "Good"

print len(newTest)

FieldChoicesInt = (
	(1,"One"),
	(2, "Two"),
	(3, "Three")
	)

for i in FieldChoicesInt:
	print "%s: %s" % (i[1], i[0])