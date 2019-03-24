
d1 = {101:"Ravi",102:"Kumar",103:"Murali"}
print(d1)
print(d1[101]) # Ravi
print(d1[103]) # Murali
# if given key not available it will return
# KeyError
# print(d1[104]) # KeyError

print("-------------------")
# Modification of a Dict
d1[101] = "Rama"
print(d1)
d1[1001] = "Krishna"
print(d1)

