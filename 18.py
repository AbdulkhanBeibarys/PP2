i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

for x in range(3):
  print(x)