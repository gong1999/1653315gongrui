print "tuple:"
a=(1,2,3)#tuple
print a
for i in a:
    print i
    print i+3
print "\n" 

print "list:"
a=[1,2,3]#list
print a
for i in a:
    print i
    print i+3
print "\n" 

print "range:"
a=range(3)#range
print a
for i in a:
    print i
    print i+3
print "\n" 

print "set:"
a={1,2,3}#set
print a
for i in a:
    print i
    print i+3
print "\n" 

print "set:"
a={1,2,3}#set
print a
print "dictionary:"
b={1:'a',2:'b',3:'c'}#dictionary
print b
for i in a:
    print b[i]
print "\n"

print "2:"
n=[]
print n
for i in range(11):
    n.append(1+i*0.1)
print n
for i in n:
    print pow(i,i)
