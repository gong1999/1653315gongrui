def calculate_circumference(r):#compute the circumference
    import numpy as np
    c=2*np.pi*r*1000
    return c
    
from sys import argv
script,r=argv#input the radius of the Earth's equator(m)
c=calculate_circumference(float(r))
print "The planet's circumference is around %d m."%c
if c>=calculate_circumference(6378):
    print"The planet's circumference is more close to Earth's circumference than Martian circumference."
elif c<=calculate_circumference(3396):
    print"The planet's circumference is more close to Martian circumference than Earth's circumference."
else:
    print"The planet's circumference is between Martian circumference and Earth's circumference."
