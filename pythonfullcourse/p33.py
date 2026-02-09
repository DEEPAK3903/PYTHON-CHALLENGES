#Numeric data type

#integer type
n = int(59)
nn = 590
print(n,nn)
print(type(n),type(nn))
print(isinstance(n,int),isinstance(nn, int))
#float type
gpa = 7.77
cgpa = float(7.67)
print(gpa, cgpa)
print(type(gpa),type(cgpa))



#Complex type
im = 5+3j
print(im)
print(type(im))
print(im.real)
print(im.imag)


#built-in functions for numbers
print(abs(gpa))
print(abs(gpa *-1))
print(round(gpa))
print(round(gpa,1))
print(round(gpa, 2))