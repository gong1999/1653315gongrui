#calculate the circumference of the Earth's equator and the Earth's surface area
pi=3.14#define pi
r=6378*1000#define the radius of the Earth's equator
c=2*pi*r#calculate the circumference of the Earth's equator
s=4*pi*r**2#calculate the Earth's surface area
print "\n\tthe circumference of the Earth's equator is %d m\n\tthe Earth's surface area is %d m^2\n"%(c,s)#output result
