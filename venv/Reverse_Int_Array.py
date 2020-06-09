count = 10**5
nums = []

#Linear growth -
#for i in range(count):
#   nums.append(i)
#nums.reverse()

#Quadratic growth -
for i in range(count):
    nums.insert(0,i)
