#find the host domain in the from field

data = 'From joey.boyer@hi-tyrone.com Sat 28 FEB 09:14:13 2015'
atpos = data.find('@') #look for the at symbol
print atpos

sppos = data.find(' ',atpos) #start at value of atpos, look for a space
print sppos

host = data[atpos+1 : sppos] #slice data from one space to the right of atpos to the space before sppos

print host
