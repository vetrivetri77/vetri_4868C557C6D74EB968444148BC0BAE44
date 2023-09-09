#implement
def fact(x):
  if x==1:
    return 1
  else:
   print(x)
   sum=x*fact(x-1)
  return(sum)
num=int(input("Enter a number:"))
if num>=-1:
  print("Factorial value",fact(num))