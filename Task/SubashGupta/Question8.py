#8. Develop a Python program to count the frequency of each element in a list and return it as a dictionary.
a=[]
n=int(input('enter length of the list :'))
print('enter the numbers ')
for i in range(n):
  x=int(input())
  a.append(x)

dict={}
for i in a:
    if i in dict :
      dict[i]+=1

    else :
      dict[i]=1

print(dict)
