print "1:"
i=1
while i<=521:
    print "I love you!"
    i=i+1
print "print times : %d\n"%(i-1)

print "2:"
import numpy as np
i=0#number
count=0#counting
t=2#target
while(i<=t):
    print i
    i=np.random.randn(1)
    count=count+1
print "i=%f"%i
print "In order to produce a number which is bigger than %f,we have to do %d times of iteration."%(t,count)
print "\n"
