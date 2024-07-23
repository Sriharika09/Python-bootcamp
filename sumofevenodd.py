''' sum of even and odd'''

x=int(input())
esum=0
osum=0
while(x!=0):
  value=x%10
  if value%2==0:
    esum+=value**2
  else:
    osum+=value**2
  x=x//10
print(esum,osum)