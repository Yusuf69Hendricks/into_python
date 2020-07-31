
n = int(input('Enter number between -6 between 2: '))
print()

if -6 < n < 2:
  for x in range(n + 7, 37, 7):
    for r in range(x,  x + 7):
        print("{:>2}".format(r), end=" ")
    print()

else:
  print("Wrong input!!")