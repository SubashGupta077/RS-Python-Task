#3 You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
def digit(b):
   b = list(map(int,b))  # Convert input to list of integers
   return b

a = input("Enter the element ")
a = list(map(int, a))  # Convert input to list of integers
a[-1]+=1
b=''.join(str(string)for string in a )
print(digit(b))
