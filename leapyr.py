'''n=int(input())
if( n%4==0 and n%100!=0):
  print(n,"is a leap year")
else:
  print("its not a leap year",n)'''

n1,n2=map(int,input().split())
for i in range(n1,n2+1):
  if(i%4==0 or i%400==0):
    print(i)