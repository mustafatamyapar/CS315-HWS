import numpy as np 
#1) 1) How are the boolean values represented?
#Boolean values in python are represented with true and false. None , False ,0, 0.0, 0j, Decimal(0), Fraction(0, 1)
#'', (), [], {}, set(), range(0) are representation for false. Any other value can be used as true.

arr = np.array(["Hello"])
arr2 = np.array([])

print(bool(None))# false
print(bool (0))#   false
print(bool (0.0))# false
print(bool (33))#  true
print(bool (""))#  false
print(bool ("abc"))# true
print(bool (arr))# true
print(bool (arr2))# false
print(bool (''))# false
print(bool (set()))# false
print(bool ({}))# false
print(bool (True))# true
print(bool (False))# false

#2)What operators are short-circuited?
#Short circuit operators are and or in python.
apple = 20
andy = (apple < 25 and apple> 10)
print("elm < 25 && elm > 10")
print(andy)
elm2 = 10
ori = (elm2 > 5 or elm2 < 8)
print("elm2 > 5 || elm2 < 8")
print(ori)
def func1():
    return True
  
def func2():
    return False
  
def func3():
    print("func3 executed")
    return True
  
def func4():
    print("func4 executed")
    return False
  
if func1() and func2():
    print("Short Circuit")
  

if func3() or func4(): #shows that func 4 is not executed.
    print("Short Circuit 2 ")


#3)How are the results of short-circuited operators computed? (Consider also function calls)
#In and operations if the first one is true both expressions are checked otherwise only the first one is checked, if both are true turns true else turns false
#but in or operation if the first expression is true second one is not checked and if one of them is true turns true.
def func():
    print("in python func") 
    return True

def func2():
    print("in python func2")
    return False

print(True and func()) # executing both
print(func() and func2()) #executing both
print(func2() and func()) #executing just func2
print(True or func2()) #not executes func2
print(func() or func2()) # just executes func
print(func2() or func()) #executing both

#4)What are the advantages about short-circuit evaluation?
#Programs will be computed faster due to not computing second expression in the or,and expression. Also as shown below
#if there would not be short circuit operation our program will crash due to exceeding array size . 
arr1 = np.array(["hello","its","me"])
i = 0
Length = 3
key = "me"
while (i < Length) and (arr1[i] != key) :
    i = i + 1

#5)What are the potential problems about short-circuit evaluation?
#If there is a side effect in the expression which is used with short circuit operation and if correctness of the program
#depends on the operation this would lead to a problem in the program.
p = 9
q = 12
while (q == p) or (q > 9)  : # it would print 4 times
    q = q - 1
    print("test")



