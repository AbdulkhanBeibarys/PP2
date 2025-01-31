mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']