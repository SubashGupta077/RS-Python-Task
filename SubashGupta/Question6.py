#1 true if t is an anagram of s, and false otherwise.

s =input('enter first word ')
t =input('enter second word ')
s=''.join(sorted(s))
t=''.join(sorted(t))
if len(s)!=len(t):
  print('false')
elif s==t:
  print(True)
else:
  print(False)
