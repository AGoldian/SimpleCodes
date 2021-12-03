# 1: The member whose number you want to find
# 2: First member
# 3: Denominator of geometric progression
bn = float(input())
b1 = float(input())
q = float(input())
n = bn/b1
counter = 0
while True:
    n = n/q
    counter += 1
    if n == 1:
        break
print(counter+1)
