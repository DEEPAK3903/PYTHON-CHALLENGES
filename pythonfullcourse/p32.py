#Boolean data type
y = True
z = bool(False)
print(z)
print(type(z))
print(isinstance(z, int))#y this line prints true? doubt
#hence resolved bool inherited in int bool is the subclass of the int.
#so instead of isinstance use type for strict check type(z)->True.
print(isinstance(z, float))
print(isinstance(z, bool))
print(type(z)is int)