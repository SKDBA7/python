#!python3
import os
os.system("cls")
Invalue = int(input("Please provide the number to check: "))
print("\n The provide number is the",Invalue,end="\n")
finalvalue = Invalue & 1
print("\n The final result of the give number is the:",finalvalue,end="\n")
if (finalvalue == 0) : 
#    print("The give value is",Invalue,"is the even",end="\n")
    Dec="odd"
else:
#    print("The given value is:",Invalue,"is the odd",end="\n")
    Dec="even"

print("We have provide the result of the given value",Invalue,"is the",Dec,end="\n")

''' 
Mistake I have done is the if & else condition is not correct, I have to check the finalvalue is 0 then it is even otherwise it is odd. then I have to change the Dec variable value accordingly. 
Mistake 
Dec=even 
Dec=odd
I have no string in the Dec variable, I have to provide the string value in the Dec variable.
Dec = "odd"    # a string value
Dec = odd      # looks for a variable named odd → NameError
'''








'''
#!python3
import os
os.system("cls")
Invalue=init(input(Please provide the number to check:))
print("\n The provide number is the",Invalue,end="\n")
finalvalue=Invalue & 1
print("\n The final result of the give number is the:",finalvalue,end="\n")
if (finalvalue == 0)
    print("The give value is",Invalue,"is the even",end="\n")
    else
    print("The given value is:",Invalue,"is the odd",end="\n")

print("We have provide the result of the given value")
'''
