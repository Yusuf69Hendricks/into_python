import math

A = input("Enter vector A:\n")
B = input("Enter vector B:\n")
A = A.split()
B = B.split()

Addition = []*len(A)
Dot = []*len(A)
RootSumA = 0
RootSumB = 0
NormA = 0
NormB = 0
DotSum = 0
for i in range(0,len(A)):
  Addition.append(eval(A[i]) + eval(B[i]))
  Dot.append(eval(A[i]) * eval(B[i]))
  DotSum += (eval(A[i]) * eval(B[i]))
  RootSumA += eval(A[i])**2
  RootSumB += eval(B[i])**2
NormA = math.sqrt(RootSumA)
NormB = math.sqrt(RootSumB)
print("A+B = " + str(Addition))
print("A.B = " + str(Dot))
print("|A| = " + str('{:2f}'.format(NormA)))
print("|B| = " + str('{:2f}'.format(NormB)))
