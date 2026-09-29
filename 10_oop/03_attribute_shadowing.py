class Chai:
    temparature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temparature)

cutting.temparature = "mild"
cutting.cup = "small"

print("After changing ", cutting.temparature)
print("Cup size is ", cutting.cup)
print("Direct look into the class ", Chai.temparature)

del cutting.temparature
del cutting.cup

print("After deleting ", cutting.temparature)  #No error because there is fallback in class which is called attribute shadowing
print("Cup size is ", cutting.cup) #Error because no fallback in class