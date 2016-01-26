def computepay(h,r):
	pay = 0

	if h > 40:
		pay = (h - 40) * 1.5  * r + 40 * r
	else:
		pay = h * r

	return pay

hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))
p = computepay(hrs,rate)
print p