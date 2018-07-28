def difference(a,b):#compute the difference between two float numbers
    return float(a)-float(b)

def calculate_circumference(r):#compute the circumference
    import numpy as np
    c=2*np.pi*r*1000
    return c

result=difference(3.0,2.5)
print"The result is %f.\n"%result

print"The circumference of the Earth's equator is %f m\n"%calculate_circumference(6378)

print"The circumference of the Martian equator is %f m\n"%calculate_circumference(3396)
