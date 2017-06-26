#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
fname = raw_input("Enter file name: ")
count = 0
floataverage = 0
converted_string = 0
average_string = 0
if len(fname) == 0:
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count += 1
    converted_string = 0
    spaces = line.find(' ')
    eol = line.find('"')
    number_string = line[spaces : eol]
    stripped_string = number_string.strip()
    try: 
        converted_string = float(stripped_string)
    except:
        print 'couldn\t convert to a string, your stuff above broke something'
    average_string += converted_string
    #print 'sum is ',average_string #used these for debugging
    #print 'count is ',count#used these for debugging
floataverage = average_string / count
print 'Average spam confidence:',floataverage

