""" This programm is to show the importance of slow but consistent 1% imporvement"""

a = 100

for i in range(0,365,1):
    a = a+(a/100)
    """print (a/100)
print ("The final value of a is", a)"""
print ("\n\nOne percent improvement leads to {x:1.2f}".format(x=a/100), "times improvement in a year!\n")