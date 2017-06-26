#prompt users for pay
hours = raw_input('How many hours did you work?')
pay = raw_input('What is your hourly rate?')
rate = float(hours)*float(pay)
rate = str(rate)
print 'Your pay rate is ' + rate
