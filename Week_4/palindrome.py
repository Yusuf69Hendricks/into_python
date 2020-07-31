start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("The palindromic primes are: ")
print()

start += 1
for i in range(start,end):
    if(str(i) == str(i)[::-1]):
        if(i>1):
            for start in range(2,i):
                if(i%start==0):
                    y = False
                    break
            else:
                print(i)