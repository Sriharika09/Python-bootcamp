'''ARMSTRONG'''
x=int(input())
sum=0
while(x!=0):
  value=x%10
  sum+=value**3
  x=x//10
if sum==x:
  print("given number is armstrong")
else:
  print("given number is not armstrong") 