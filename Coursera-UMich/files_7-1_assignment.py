#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt
filename = raw_input('Enter your file name: ')
try:
    fh = open(filename)
except:
    print 'Invalid filename',filename
    exit()

for lines in fh:
    lines = lines.upper()
    lines = lines.rstrip()
    print lines
