#9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input('Enter file:')
if len(name) == 0:
    name = 'mbox-short.txt'
handle = open(name, 'r')
#text = handle.read()
sender_list = []
lst = list()
counts = {}

for lines in handle:
	if not lines.startswith("From") : continue
	if lines.startswith("From:") : continue
	lst = lines.split()
	lst_item = lst[1]
	sender_list.append(lst_item)

#print sender_list,'\n\n'

for name in sender_list :
	counts[name] = counts.get(name,0) + 1
#print counts

bigcount = None
bigname = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigname = word
        bigcount = count

print bigname,bigcount