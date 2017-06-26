#prompt_pay_assignment2.py - this adds an if/then statement based on number of hours worked (if > 40 do X if < 40, do Y)
#looking specifically for string to float with no text
hours = raw_input('Enter Hours worked')
rate = raw_input('Enter pay rate')
try:
	hours = float(hours)
	rate = float(rate)
except:
	print 'Please enter numeric input'
	quit()
ot_hours = hours%40
if hours <= 40 :
	pay = hours*rate
else:
	pay = (40*rate) + (ot_hours * (rate*1.5))
print pay