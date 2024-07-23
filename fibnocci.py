''' fibnoccis'''
n=int(input())
f1=0
f2=1
fn=f2
count=1
while count<=n:
  print(fn,end=" ")
  count+=1
  f1=f2
  f2=fn
  fn=f1+f2
print()