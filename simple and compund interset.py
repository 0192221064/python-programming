p=int(input(" enter p value" ))
t=int(input(" enter t value" ))
r=int(input(" enter r value" ))
n=int(input(" enter n value" ))
si=(p*t*r)/100
ci= (p*(1+r/n)**n-p)
print(si,ci)
