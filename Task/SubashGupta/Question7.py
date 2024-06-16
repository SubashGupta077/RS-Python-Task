#7. Alfi and Roy go to shopping.on each product of MRP Alfi will pay min of the prime factor and rest Roy will pay.Find Roy's ammount.
def prime(x):
  for j in range(2,x+1):
   if x%j==0:
    break

  return j
R=T=0
n=int(input('no of product brought :'))
a=[]
for i in range(1,n+1):
  r=int(input(f'enter MRP of product {i} :'))
  T=T+r
  a.append(r)

for i in range(0,n) :
    x=a[i]
    R=R+prime(x)
    print(f'Roy has to pay rupee {a[i]-prime(x)} on product {i+1}')

t=T-R
print(f'Roy has to pay a total of {t} rupee')

