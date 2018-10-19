p1price = 295000
p1revenue = 15300
p1tax = 2894
insurence = 1500

print (p1price)    
p1afterd = ((p1price)*(0.9))
print (p1afterd)
p1mort = (((p1afterd)/(100000))*5600)
print (p1mort)
p1mrev = (((p1revenue) - (p1mort) - (p1tax) - (insurence))/12)          
print (p1mrev)

