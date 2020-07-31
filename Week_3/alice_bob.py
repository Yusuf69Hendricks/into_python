# Enter
#   # get input for a 
#   # get input for b
#   # convert a into list
#   # convert b into list
#   FOR (length=3)
#     IF a[index] > b[index]
#       increment alice`s score by 1
#     ELSE IF a[index] < b[index]
#       increment bobs score by 1
#     ELSE 
#       do nothing
#     ENIF
#   ENDFOR
# Exit   

# Alice and BOB
# Name: Yusuf Hendricks 
# Date: 22nd May 2020


a = list(map(int, input().split()))
b = list(map(int, input().split()))

aliceScore = sum([(1 if a[i] > b[i] else 0)for i in range(3)])
bobScore = sum([(1 if a[i] < b[i] else 0)for i in range(3)])
print(aliceScore, bobScore)











# 2nd sollution

# for i in range(3):
#   if a[i]>b[i]:
#     aliceScore = aliceScore + 1
#   if a[i]<b[i]:
#     bobScore = bobScore + 1