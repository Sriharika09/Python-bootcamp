'''n=int(input())
for i in range(1,n+1):
  if(n==1):
    print("neither prime nor composite")
  elif(n%2==0 or n%3==0 or n%5==0):
    print("not prime")
  else:
    print("is prime")'''



                                                                                                                                
'''count=0
r=n**0.5
for i in range(2,int(r+1)):
  if n%i==0:
    count+=1
    break
if count==1:
  print("not prime")
else:
  print("prime")'''


'''print all prime nums till given range
n=int(input())
if(n>2 and n>3 and n>5):
  print("2,3,5,",end="")
for i in range(0,n+1):
  if(i%2!=0 and i%3!=0 and i%5!=0 and i!=1):
    print(i,end=",")'''



n1,n2=map(int,input().split())
for i in range(n1,n2+1):
  count=0
  for j in range(2,i):
    if(i%j==0):
      count+=1
      break
  if count==0 and i!=1 and i!=0:
    print(i)