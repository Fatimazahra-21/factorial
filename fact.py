while true : 
n = int(input("entrer n :"))
if n >=0 :
break
if n == 0 :
print("la factorielle de 0 est 1")
else :
F = 1
for i in range(2,n+1):
F = F*i
print("la factorielle de ",n,"est :",F)
