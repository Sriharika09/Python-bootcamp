"""a,b=map(int,input().split())
print("sum=",a+b,"diff=",a-b,"product=",a*b,"division=",a//b,"modulus=",a%b)
print("power=",a**b) """
'''age=int(input())
if(age>=18 and age<24):
  print("only 2 wheeler")
elif(age>=24 and age<45):
  print("2 and 4 wheeler")
elif(age>=45 and age<60):
  print("2, 4 and 6 wheeler")
else:
  print("none") '''
x=int(input)
if x>0:
  if x%2==0:
    print("positive even")
  else:
    print("positive odd")
elif x<0:
  if x%2==0:
    print("negative even")
  else:
    print("negative odd")
else:
  print("zero is neither even nor odd and neither -ve nor +ve")

