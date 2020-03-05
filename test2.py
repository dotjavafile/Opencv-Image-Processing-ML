i= result =1.00
j =c= 0
while i > 0:
    i = float(input(""))
    if i>=0 :
        c+=i
        j+=1
    else:
        break
result=c/j
print("%.2f" %(result))