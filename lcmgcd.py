a,b=map(int,input().split())
'''while b!=0:
  a,b=b,a%b
print("GCD of 2 numbers is",a)'''
if (a%b==0 or b%a==0):
  print("lmc=",b)
else:
  print("lcm=",a*b)
