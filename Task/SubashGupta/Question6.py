#6. Given an array, A, of length N. Find the absolute difference between the smallest and largest prime number in array A.
def go(x):
  if x==2:
    count=0
  elif x==1 or x==0 :
    count=1
  else:
   for i in range(2,x) :
    if x%i==0:
      count=1
      break
    else :
     count=0
  return count

n=int(input('enter the length of the array :'))
print('enter the numbers ')
a=[]
p=[]
while(len(a)<n):
   x=int(input())
   a.append(x)

for i in range(0,n):
      x=a[i]
      t=go(x)
      if t==0 :
        p.append(a[i])

p=sorted(p)
if len(p)<2:
  print('1')
else:
 f= p[-1]-p[0]
 print(f'difference between largest and smallest prime number {p[-1]} and {p[0]} is ', f)
