

hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter rate:"))

pay = 0

if hrs > 40:
	pay = (hrs - 40) * 1.5  * rate + 40 * rate
else:
	pay = hrs * rate

print pay