import math
p=4
q=5
n=p*q
e=3
phi=(p-1)*(q-1)
while(e,phi):
    if (math.gcd(e,phi)==1):
        break
    else:
        e=e+1
k=7
d=(1+(k*phi))/e
msg=12.0
print("message data",msg)
c=pow(msg,e)
c=math.fmod(c,n)
print("encryption data",c)
m=pow(c,d)
m=math.fmod(c,d)
print("original message sent data",m)
