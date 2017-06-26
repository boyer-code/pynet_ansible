hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
r = float(rate)
ot_hrs = h%40
#print ot_hrs, ' hours of overtime'
ot_pay = ((r*1.5)*ot_hrs)
#print ot_pay,'is your overtime pay'
straight_pay = ot_pay+(r*(h-ot_hrs))
print straight_pay
