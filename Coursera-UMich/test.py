banana = raw_input('Enter the file name: ')
try:
    banana = open(banana)
except:
    print 'File cannot be opened:',banana
    exit()
for potato in banana:
    potato = potato.rstrip()
    if potato.startswith('From:') :
        print potato
