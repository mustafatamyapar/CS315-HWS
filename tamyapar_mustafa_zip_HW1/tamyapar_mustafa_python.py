import numpy as np 
#1) What types are legal for subscripts?
#In Python integer, float, double and boolean,char are allowed for subcripting.
city = np.array(["izmir",  "ankara" , "istanbul", "aydin", "mugla"])
for x in city:
    print(x)
 #Accessing elements in python arrays.
print("The first element is: ")
print(city[0])
print("The last element is: ")
print(city[-1])

#2)Are subscripting expressions in element references range checked?
#Range check takes place in run time.
#print("Range Check")
#print(city[10]); #Gives an error due to range of the array being 4.

#4)When does allocation takes place?
#Allocation takes place in rune time because this code snippet is compiling but gives an runtime error.
#alloca = arr4[0]

#5)Are ragged or rectangular multidimensional arrays allowed, or both?
#In Python language, in Numpy library both ragged and rectangular arrays are allowed.

print("Rectangular multidimensional array example: ")
rectangular = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
print(rectangular)
print("Ragged multidimensional array example: ")
ragged = np.array([[1],[2,2],[3,3,3],[4,4,4,4]],dtype=object)
print(ragged)

#6)Can array objects be initialized?
#In python array objects can be created.  
print("Object array example:")
elt = np.array(['b', 3, 3.5])
print(elt)

#7)Are any kind of slices supported?
#Python supports slices.
print("Slice example:")
sauce = np.array(['k','m','s','h','b'])
print(sauce)
print(sauce[0:2])# [k,m]
print(sauce[3:])#[h,b]
print(sauce[:2])#[k,m]
print(sauce[:] )#Copies whole array

#8)Which operators are provided?
#In python arrays +, *, /, ==, !=,[],=[],>=,
# @, operators are allowed.
arrOp= np.array([1])
arrOp2 = np.array([2,20,30,14,28])
arrOp3 = np.array([9,3,5,2,10])

arrOp4 = arrOp3 + arrOp2 #+(shapes of the arrays should be same)
print("+ operation with 2 arrays ")
print(arrOp4)

arrOp8 = arrOp3 + 2 #+
print("+ operation with integer ")
print(arrOp8)

arrOp11 = arrOp3 - 2 #-
print("- operation with integer ")
print(arrOp11)

arrOp6 = arrOp3 * 2 #*
print("* operation with integer ")
print(arrOp6)

arrOp7 = arrOp3 * arrOp2 #*(2 arr)
print("* operation with 2 arr ")
print(arrOp7)

arrOp9 = arrOp3 / arrOp2 #/(2 arr)
print("/ operation ")
print(arrOp9)

print("== operation ")
print(arrOp4 == arrOp3) #==

print("!= operation ")
print(arrOp4 != arrOp3) #!=

arrOp30 = np.array([1]) #[]
print("[] operation ")
print(arrOp30)

arrOp30[0] = 23 #=[]
print("=[] operation ")
print(arrOp30)

arrOp10 = arrOp2 >= 20 #>=
print(">= operation ")
print(arrOp30)

multi_dim1 = np.array([[3,2],[0,1]])
multi_dim2 = np.array([[3,1],[2,1]])

print("@(matrix multip) operation ")
print(multi_dim1 @ multi_dim2) #matrix multiplication @
