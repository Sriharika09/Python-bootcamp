''' MR.X IS TRYING TO CREATE A NEW PASSWORD FOR HIS INSTA ACCOUNT 
THESE ARE THE REQUIRED CONDITIONS FOR CREATING A NEW PASSWORDS
1. MIN LENGTH IS 8 MAX IS 15
2. ONLY @,/  IS ALLOWED IN THE PW
3. NO SPACES ARE ALLOWED
4.ONLY ALPHA NUMARICS ARE ALLOWED
YOU ARE SUPPOSED TO PRINT WEAK IF LENGTH IS EXCATE 8
MEDIAM -LENGTH IS BETWEEN 8-12
STRONG- LENGTH IS BETWEEN 12-15
 '''

s=input()
count=0
symbols="@/"
numbers="0123456789"
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ"
if len(s)==8:
  print("PASSWORD IS WEAK")
elif len(s)>8 and len(s)<=12:
  print("PASSWORD IS MEDIUM")
elif len(s)>12 and len(s)<=15:
  print("PASSWORD IS STRONG")
for i in range(len(s)):
  if s[i]==" ":
    print("spaces are not allowed")
    break
  elif("@" or "/" not in s):
    count+=1
  elif( s[i] not in symbols,numbers,letters):
    print("follow the instructions")
if count>=3:
  print("password must contain @ or /")

''' '''
'''SORT ELEMENTS 
l=list(map(int,input().split()))
l.sort()
print(*l)
l.reverse()
print(*l) '''



  
