
t1 = () #Empty Tuple
print(type(t1))

t2 = (10,20.25,"Ravi",False)
print(t2)
print(t2[0]) # 10
print(t2[-1]) # False

# t2[3] = "Krishna"  Error
print(t2)

print("---------------------")

t3 = 10,10.25,"Sathya" # Packing
print(t3)
print(type(t3))

a,b,c = t3  # un_packing
print(a,type(a))# 10 <class 'int'>
print(b,type(b))# 10.25 <class 'float'>
print(c,type(c))# Sathya <class 'str'>

print("----------------------")

t1 = () # Empty Tuple
print(t1) # ()
print(type(t1)) # <class 'tuple'>

t2 = (90)
print(t2) #90
print(type(t2))# <class 'int'>

t3 = (90,)
print(t3)
print(type(t3))


