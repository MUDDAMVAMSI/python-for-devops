import sys
type= sys.argv[1]

if type=="t2.micro": #value must be in quotes
    print("the instance is t2.micro")
else:
    print("the instance is not t2.micro")
    
#if you want more than 2 conditions then you can use elif statements

import sys
type= sys.argv[1]

if type=="t2.micro": 
    print("the will charge you 2 dollars per day")
elif type=="t3.medium":
    print("this will charge you 4 dollars per day")
elif type=="t2x.large":
    print("this will charge 10 dollars per day")
#you can write as many as elif statements
else:
    print("the is not applicable")

