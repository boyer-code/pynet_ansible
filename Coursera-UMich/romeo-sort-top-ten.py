fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

for val, key in lst[:10] :
    print key, val

#even shorter
#c = {'a':10, 'b':1, 'c':22}
#print sorted( [(v,k) for k,v in c.items() ] )
#[(1, 'b'), (10, 'a'), (22, 'c')]
#
#