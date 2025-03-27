#import just one thing
# from mymodule import greet

# print(greet("Blend"))

#imports all
import mymodule

 



print(mymodule.greet("Blend"))

cal = mymodule.Calculator()

print(cal.add(3, 5))
print(cal.subtract(10, 4))

#import math
#result = math.sqrt(25)

# from math import sqrt, pi
# print("square root of 36 is:", sqrt(36))
# print("Value of PI is:", pi)

from math import sqrt as square_root

print("square root of 36 is:", square_root(36))

from my_package.utils import greet 