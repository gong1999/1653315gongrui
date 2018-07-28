print "set:"
s1={1,2,3,'a','b','c'}#set
s2={1,1,1,'a','b','c'}#set
s3={1,2,3,'a','a','a'}#set
print "s1:"
print s1
print "s2:"
print s2
print "s3:"
print s3,"\n"
print "dictionary:"
d1={'a':1,2:4,(1,2):7,"extra1":'a',"extra2":'b',"extra3":'c'}#dictionary
d2={'a':2,2:5,(1,2):8,"extra1":'a',"extra2":'b',"extra3":'c'}#dictionary
d3={'a':3,2:6,(1,2):9,"extra1":'a',"extra2":'b',"extra3":'c'}#dictionary
print "d1:"
print d1
print "d2:"
print d2
print "d3:"
print d3,"\n"

print "d1['a']:"
print d1['a'],"\n"

print "s2.add(d3['a']):"
s2.add(d3["a"])
print s2,"\n"

print "d2['set']=s1:"
d2["set1"]=s1
print d2,"\n"

print "s1[0]:(error)"
print s1[0],"\n"#error

